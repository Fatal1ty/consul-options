# encoding: utf8

from __future__ import absolute_import

import consul.base
from consul.std import HTTPClient


class LazyHTTPClient(HTTPClient):
    def setup(self, host, port, scheme):
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
        if item in ('__getter__', '__setter__') +\
                tuple(object.__getattribute__(self, '__dict__').keys()):
            return object.__getattribute__(self, item)
        value = self.__getter__(item)
        if value is not None:
            try:
                default = object.__getattribute__(self, item)
                return type(default)(value)
            except AttributeError:
                return value
        else:
            value = object.__getattribute__(self, item)
            self.__setter__(item, value)
            return value


class ConsulKV(KeyValue):
    def __init__(self, server, parent=None):
        self.__consul__ = server
        self.__parent__ = parent.strip('/')

    def __getter__(self, key):
        path = self.__parent__ + '/' + key if self.__parent__ else key
        index, data = self.__consul__.kv.get(path)
        value = data['Value'] if data else None
        return value

    def __setter__(self, key, value):
        path = self.__parent__ + '/' + key
        self.__consul__.kv.put(path, str(value))


class CachedConsulKV(ConsulKV):
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
        self.consul = LazyConsul()

    def setup(self, host, port, scheme):
        self.consul.http.setup(host, port, scheme)


consul = ConsulOptions()
