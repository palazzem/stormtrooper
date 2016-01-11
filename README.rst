============
Stormtrooper
============

If `Django`_ is your first choice for the conquest of the Internet, you need something that spawns quickly your
Django applications!

Getting started
---------------

The Internet is your target; start spawning your first expendable stormtrooper:

.. code-block:: bash

    $ mktmpenv
    $ pip install cookiecutter
    $ cookiecutter https://github.com/palazzem/stormtrooper

    # it outputs
    Cloning into 'stormtrooper'...
    remote: Counting objects: 83, done.
    remote: Compressing objects: 100% (52/52), done.
    remote: Total 83 (delta 34), reused 70 (delta 23), pack-reused 0
    Unpacking objects: 100% (83/83), done.
    Checking connectivity... done.

Now you should give a name to your stormtrooper. Wait, it's a stormtrooper. They don't have a name.

.. code-block:: bash
    app_name [stormtrooper]: stormtrooper

Stormtrooper helmet
-------------------

A good design, starts from the head: monitoring

NewRelic
~~~~~~~~

Configure your `NewRelic`_ monitoring service:

.. code-block:: bash
    $ newrelic-admin generate-config thisISnotAlicenseKEY newrelic.ini

.. _NewRelic: http://newrelic.com/

Stormtrooper armor
------------------

Security concerns.

Starting the assault
--------------------

Just check the ``README.rst`` file present in the newly created app.

License
-------

``Stormtrooper`` is released under the terms of the **BSD license**. Full details in ``LICENSE`` file.

.. _Django: https://www.djangoproject.com/

Credits
-------

* `Cookiecutter`_ for template spawning!

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
