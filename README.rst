django-categories-i18n
======================

A simple categories model that supports translations.
Improvements are welcome!


Installation
============

First install the module, preferably in a virtual environment.
It can be installed from PyPI:

.. code-block:: bash

    pip install django-categories-i18n

Add ``categories_i18n`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS += (
        'categories_i18n',
    )


Usage
=====

* Link to the ``categories_i18n.models.Category`` model in your application.


Improving this package
======================

This module is designed to be usable for other projects too.
In case there is anything you didn't like about it,
or think it's not flexible enough, please let us know.
We'd love to improve it! Pull requests are welcome too. :-)
