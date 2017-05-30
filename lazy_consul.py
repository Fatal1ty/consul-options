# encoding: utf8

from __future__ import absolute_import
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

import consul.base
from consul.std import HTTPClient
from six import with_metaclass


class LazyHTTPClient(HTTPClient):
    def setup(self, url=None, host=None, port=None, scheme=None):
        if url:
            o = urlparse(url)
            self.host = o.hostname
            self.port = o.port
            self.scheme = o.scheme
            self.base_uri = url
        else:
            self.host = host
            self.port = port
            self.scheme = scheme
            self.base_uri = '%s://%s:%s' % (scheme, host, port)


class LazyConsul(consul.base.Consul):
    def connect(self, host, port, scheme, verify=True):
        return LazyHTTPClient(host, port, scheme, verify)


class KeyValue(object):
    def __getter__(self, key):
        raise NotImplementedError

    def __setter__(self, key, value):
        raise NotImplementedError

    def __getattribute__(self, item):
        if item in ('__getter__', '__setter__', '__path__') +\
                tuple(object.__getattribute__(self, '__dict__').keys()):
            return object.__getattribute__(self, item)
        value = self.__getter__(item)
        if value is not None:
            try:
                default = object.__getattribute__(self, item)
                value = str(value.decode('utf8'))  # for compatibility
                return type(default)(value)
            except AttributeError:
                return value
        else:
            try:
                value = object.__getattribute__(self, item)
            except AttributeError:
                path = self.__path__
                full_path = '%s/%s' % (path, item) if path else item
                msg = "There is no such key '%s'" % full_path
                raise AttributeError(msg)
            self.__setter__(item, value)
            return value

    @property
    def __path__(self):
        mro = object.__getattribute__(self, '__class__').mro()
        path = []
        for base in mro:
            if base in (ConsulKV, CachedConsulKV):
                break
            else:
                try:
                    name = object.__getattribute__(base, '__key__')
                except AttributeError:
                    name = base.__name__.lower()
                path.append(name)
        return '/'.join(reversed(path))


class ConsulOptionsMeta(type):
    def __init__(cls, name, bases, clsdict):
        if name not in ('ConsulKV', 'CachedConsulKV'):
            path = []
            for c in cls.mro():
                if c in (ConsulKV, CachedConsulKV):
                    break
                else:
                    path.append(c)
            po = ConsulOptions.__global__
            for c in reversed(path):
                try:
                    key = object.__getattribute__(c, '__key__')
                except AttributeError:
                    key = object.__getattribute__(c, '__name__').lower()
                try:
                    o = object.__getattribute__(po, key)
                except AttributeError:
                    o = c(ConsulOptions.__global__.__consul__)
                    object.__setattr__(po, key, o)
                object.__setattr__(o, '__key__', key)
                po = o
        super(ConsulOptionsMeta, cls).__init__(name, bases, clsdict)


class ConsulKV(with_metaclass(ConsulOptionsMeta, KeyValue)):
    def __init__(self, server):
        self.__consul__ = server

    def __getter__(self, key):
        path = self.__path__
        path = path + '/' + key if path else key
        index, data = self.__consul__.kv.get(path)
        # index, data = None, None
        value = data['Value'] if data else None
        return value

    def __setter__(self, key, value):
        path = self.__path__
        path = path + '/' + key if path else key
        self.__consul__.kv.put(path, str(value))


class CachedConsulKV(with_metaclass(ConsulOptionsMeta, ConsulKV)):
    def __init__(self, *args, **kwargs):
        super(CachedConsulKV, self).__init__(*args, **kwargs)
        self.__cache__ = {}

    def __getter__(self, key):
        value = self.__cache__.get(key)
        if not value:
            value = super(CachedConsulKV, self).__getter__(key)
            self.__cache__[key] = value
        return value


class ConsulOptions(object):
    def __init__(self):
        self.__consul__ = LazyConsul()

    def setup(self, url=None, host=None, port=None, scheme=None):
        self.__consul__.http.setup(url, host, port, scheme)


consul = ConsulOptions()
ConsulOptions.__global__ = consul
