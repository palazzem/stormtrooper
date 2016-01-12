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

Production
~~~~~~~~~~

These environment variables are required when using the ``production.py`` settings;
in development or testing mode, they are not required and no SSL connection will be used.

* ``SECRET_KEY``
* ``DJANGO_ASSETS_ROOT`` (default: project root folder)
* ``DJANGO_SETTINGS_MODULE``
* ``DJANGO_SECURE_SSL_REDIRECT`` (default: ``True``)
* ``DJANGO_SESSION_COOKIE_SECURE`` (default: ``True``)
* ``DJANGO_ALLOWED_HOSTS`` (default: ``None``)
* ``DJANGO_EMAIL_BACKEND`` (default: ``django.core.mail.backends.smtp.EmailBackend``)
* ``DJANGO_FROM_EMAIL``
* ``EMAIL_HOST``
* ``EMAIL_HOST_PORT``
* ``EMAIL_HOST_USER``
* ``EMAIL_HOST_PASSWORD``
* ``UWSGI_SOCKET``: sets the unix socket path
* ``UWSGI_PROCESSES``: sets the number of uWSGI processes
* ``LOGSTASH_HOST`` (default: ``127.0.0.1``)
* ``LOGSTASH_PORT`` (default: ``5000``)
* ``NEW_RELIC_CONFIG_FILE``: sets the NewRelic configuration file ``newrelic.ini``
* ``SENTRY_DSN``: sets the ``dsn`` value, collected in the Sentry setup page

Services
~~~~~~~~

These environment variables define the service string connections. You may set
these values according to your development environment. If you are using ``docker``,
just change ``DATABASE_URL`` and ``CACHE_URL`` with your linked container URLs.

* ``DATABASE_URL`` (default: ``postgres://devel:123456@127.0.0.1:5432/{{ cookiecutter.app_name }}``)
* ``CACHE_URL`` (default: ``redis://127.0.0.1:6379/1``)

If you're using ``dev.py`` or ``test.py`` settings, just configure *Services* variables
(if needed).
