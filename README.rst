consul-options - Define and use your project settings without pain
===================================================================

.. image:: https://travis-ci.org/Fatal1ty/consul-options.svg?branch=master
    :target: https://travis-ci.org/Fatal1ty/consul-options

.. image:: https://img.shields.io/pypi/v/consul-options.svg
    :target: https://pypi.python.org/pypi/consul-options

.. image:: https://img.shields.io/pypi/pyversions/consul-options.svg
    :target: https://pypi.python.org/pypi/consul-options/

.. image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
    :target: https://opensource.org/licenses/Apache-2.0


How often do you wonder where to store the project settings? When your project is small
it is not a big problem. But if your big project consists of dozens of microservices
then there is the problem of centralized configuration management. The Сonsul have a key/value
storage that is ideal for this.

With **consul-options** you can define and use options in your code by a simple and elegant way.
Just take a look at the example:

.. code-block:: python

    class DB(ConsulKV):
        pass


    class Users(DB):
        host = '127.0.0.1'
        port = 5432
        user = 'postgres'
        password = 'postgres'

        dbname = 'users'


    class Orders(DB):
        host = '127.0.0.1'
        port = 5432
        user = 'postgres'
        password = 'postgres'

        dbname = 'orders'

Now you can access to the option values in a clear way:

.. code-block:: python

    from consul_options import options

    print options.db.users.host
    print options.db.orders.dbname

**consul-options** automagically creates folders and keys with default values defined above
in Consul and later read them from there. So if anyone will change the value of *db/orders/host* key
to something different in Consul then you will get that value.

How project options stored in Consul
------------------------------------

When you declare a new class based on **ConsulKV** default bahavior is
creation a *folder* in Consul key/value storage with name of your class in lowercase.
Each class attribute you define will have mapping to key *folder.key*.
If you want to change this name you can use reserved class attribute **__key__** as shown below:

.. code-block:: python

    class WorkerOptions(ConsulKV):
        __key__ = 'worker'

        host = '127.0.0.1'
        port = 80

After that you can access to the option with "worker" in path:

.. code-block:: python

    from consul_options import options

    print options.worker.host
    print options.worker.port

To create hierarchial key structure you can take advantage of usual class hierarchy:

.. code-block:: python

    from consul_options import ConsulKV, options

    class WorkerOptions(ConsulKV):
        __key__ = 'worker'

        host = '127.0.0.1'
        port = 80

    class DB(WorkerOptions):
        host = '127.0.0.1'
        port = 5432
        user = 'postgres'
        password = 'postgres'

    print options.worker.db.host  # 'host'
    print options.worker.db.port  # 5432

It is also possible to create keys at root level with class attribute **__root__**:

.. code-block:: python

    class RootOptions(ConsulKV):
        __root__ = True

        host = '127.0.0.1'
        port = 80

    print options.host
    print options.port


Compatibility
-------------

consul-options is compatible with both Python 2 and Python 3.


Installation
------------

Use pip to install::

    $ pip install consul-options


License
-------

consul-options is developed and distributed under the Apache 2.0 license.
