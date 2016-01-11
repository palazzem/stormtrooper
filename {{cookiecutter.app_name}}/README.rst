=============
Empty project
=============

Steps
-----

1. Add a proper license in the ``LICENSE`` file
2. Add authors and/or contributors in the ``AUTHORS`` file

Getting started
---------------

The service may be wrapped using NewRelic. In this case, launch the production service with the
following command:

.. code-block:: bash

    $ newrelic-admin run-program uwsgi

Altering the configuration
--------------------------

You may set the following variables to alter the default behavior of the app:

* ``NEW_RELIC_CONFIG_FILE``: defaults to ``newrelic.ini``
