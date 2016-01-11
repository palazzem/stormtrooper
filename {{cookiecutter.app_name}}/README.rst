=============
Empty project
=============

Getting started
---------------

The service may be wrapped using NewRelic. In this case, launch the production service with the
following command:

.. code-block:: bash

    $ newrelic-admin run-program uwsgi

Altering the configuration
--------------------------

You may set the following variables to alter the default behavior of the app:

* ``NEW_RELIC_CONFIG_FILE``: set the NewRelic configuration file ``newrelic.ini``
* ``SENTRY_DSN``: set the ``dsn`` value, collected in the Sentry setup page
* ``UWSGI_SOCKET``: set the unix socket path
* ``UWSGI_PROCESSES``: set the number of uWSGI processes
