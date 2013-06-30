Installation from source
________________________

Requirements
------------

RestAuth has the following requirements:

* `Python`_ 2.6.5 or later or Python 3.2 or later
* `Django`_ 1.5 or later - RestAuth is written as a Django project
* `RestAuthClient`_ 0.6.1 or later

Get source
----------

From git
++++++++

This project is developed on `git.fsinf.at <https://git.fsinf.at/>`_. You can
view the source code at `git.fsinf.at/restauth/django
<https://git.fsinf.at/restauth/django>`_. To clone the repository to a directory
named "RestAuth", simply do:

.. code-block:: bash

   git clone http://git.fsinf.at/restauth/django.git DjangoRestAuth

.. NOTE:: A mirror of this git-repository is available
   `on github <https://github.com/matigit/django-restauth>`_.

Older versions are marked as tags. You can view available tags with
:command:`git tag -l`. You can use any of those versions with :command:`git
checkout`, for example :command:`git checkout 1.0`.  To move back to the newest
version, use :command:`git checkout master`.

If you ever want to update the source code, just use:

.. code-block:: bash

   python setup.py clean
   git pull

... and do the same as if you where
:ref:`doing a new installation <install_from-source_installation>`.

Official releases
+++++++++++++++++

You can download official releases of RestAuth `here
<https://server.restauth.net/download>`_. The latest release is version
|restauth-latest-release|.

.. _install_from-source_installation:

Installation
------------

Installation itself is very easy. Just go to the directory where your source is
located ("RestAuth" in the above example) and run:

.. code-block:: bash

   python setup.py build
   python setup.py install

Once you have installed RestAuth, you can go on :doc:`configuring your webserver
<../config/webserver>` and :doc:`configuring RestAuth <../config/restauth>`.

Next steps
----------
Now that you have installed RestAuth, you still need to

#. :doc:`configure your webserver <../config/webserver>`
#. :doc:`setup your database <../config/database>`
#. :doc:`configure RestAuth <../config/restauth>`

Run tests
---------

RestAuth features an extensive test suite. You can run those tests using:

.. code-block:: bash

   python setup.py test

Note that you can run these tests even if you already installed RestAuth or
locally configured your RestAuth installation. The tests will *always* use their
own temporary database.

.. _source-update:

Updating the source
-------------------

To update the source code, just run:

.. code-block:: bash

   python setup.py clean
   git pull
   python setup.py install
