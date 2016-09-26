=============================
django-staticpages
=============================

.. image:: https://badge.fury.io/py/django-staticpages.png
    :target: https://badge.fury.io/py/django-staticpages

.. image:: https://travis-ci.org/fgmacedo/django-staticpages.png?branch=master
    :target: https://travis-ci.org/fgmacedo/django-staticpages

Another static page Django app.

Documentation
-------------

The full documentation is at https://django-staticpages.readthedocs.org.

Quickstart
----------

Install django-staticpages::

    pip install django-staticpages

Include it on INSTALLED_APPS::

    'staticpages',

Add to urls:

.. code-block:: python

    url(r'^(?P<menu_slug>[\w\-]+)/', include('staticpages.urls', namespace='staticpages')),

Add to middlewares:

.. code-block:: python

    MIDDLEWARE_CLASSES = [
        ...
        'staticpages.middleware.StaticPageFallbackMiddleware',
    ]


Then use it in a template.

To load all pages inside a menu:

.. code-block:: django

    {% load staticpages_tags %}

    {% get_pages_from_menu 'about-us' as about_us_pages %}

    {% for i in about_us_pages %}
        Title: {{i.title}}
        ...
    {% endfor%}

To get a specific page:

.. code-block:: django

    {% load staticpages_tags %}

    {% get_page 'about-us/vision' as vision %}
    Title: {{vision.title}}

To get a URL to a specific page:

.. code-block:: django

    {% load staticpages_tags %}

    <a href="{% get_page_url 'about-us/vision' %}">Our vision</a>


Features
--------

* Build menus from static pages.
* Get a page from his slug.
* Redirect to a link.

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ python runtests.py
