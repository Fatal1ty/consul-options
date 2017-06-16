consul-options - Define and use your project settings without pain
===================================================================

.. image:: https://travis-ci.org/Fatal1ty/aiofcm.svg?branch=master
    :target: https://travis-ci.org/Fatal1ty/aiofcm

.. image:: https://img.shields.io/pypi/v/aiofcm.svg
    :target: https://pypi.python.org/pypi/aiofcm

.. image:: https://img.shields.io/pypi/pyversions/aiofcm.svg
    :target: https://pypi.python.org/pypi/aiofcm/

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


Compatibility
-------------

consul-options is compatible with both Python 2 and Python 3.


Features
--------

* Internal connection pool which adapts to the current load
* Sending notification and/or data messages
* Ability to set TTL (time to live) for messages
* Ability to set priority for messages
* Ability to set collapse-key for messages


Installation
------------

Use pip to install::

    $ pip install consul-options


License
-------

consul-options is developed and distributed under the Apache 2.0 license.
