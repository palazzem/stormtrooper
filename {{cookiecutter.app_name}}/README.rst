=============
Empty project
=============

Getting started
---------------

The service may be wrapped using NewRelic. In this case, launch the production service with the
following command:

.. code-block:: bash

    $ newrelic-admin run-program uwsgi

Settings
--------

``{{ cookiecutter.app_name }}`` requires the following settings in order to work as expected.

Core
~~~~

These environment variables are required when using the ``production.py`` settings;
in development or testing mode, they are not required and no SSL connection will be used.

* ``DJANGO_SECURE_SSL_REDIRECT`` (default: ``True``)
* ``DJANGO_SESSION_COOKIE_SECURE`` (default: ``True``)
* ``DJANGO_ALLOWED_HOSTS`` (default: ``None``)
* ``NEW_RELIC_CONFIG_FILE``: sets the NewRelic configuration file ``newrelic.ini``
* ``SENTRY_DSN``: sets the ``dsn`` value, collected in the Sentry setup page
* ``UWSGI_SOCKET``: sets the unix socket path
* ``UWSGI_PROCESSES``: sets the number of uWSGI processes

Services
~~~~~~~~

These environment variables define the external services access. You may set
these values according to your development environment. If you are using ``docker``,
just change ``DATABASE_URL`` and ``CACHE_URL`` with your linked container URLs.

* ``DATABASE_URL`` (default: ``postgres://devel:123456@127.0.0.1:5432/runaway``)
* ``CACHE_URL`` (default: ``redis://127.0.0.1:6379/1``)
* ``DJANGO_EMAIL_BACKEND`` (default: ``django.core.mail.backends.console.EmailBackend``)
* ``EMAIL_HOST``
* ``EMAIL_HOST_PORT``
* ``EMAIL_HOST_USER``
* ``EMAIL_HOST_PASSWORD``

Altering the configuration
--------------------------

You may set the following variables to alter the default behavior of the app:
