===========
django-yasp
===========

.. image:: https://badge.fury.io/py/django-yasp.png
    :target: https://badge.fury.io/py/django-yasp

.. image:: https://travis-ci.org/fgmacedo/django-yasp.png?branch=master
    :target: https://travis-ci.org/fgmacedo/django-yasp

Another static page Django app.

Main features:

* It does not use the ``sites`` app.
* Allows grouping pages by a menu.
* Optional template overriding by page.
* Template tags to get a page or a group of pages by menu.
* Page has an image field (optional).
* Page itens can specify a link (redirect).
* Pages can be orderable (if `django-admin-sortable2`_ is installed).


.. _django-admin-sortable2: https://github.com/jrief/django-admin-sortable2

Quickstart
----------

Install django-yasp::

    pip install django-yasp

Include it on INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'yasp',
    ]


Add to urls:

.. code-block:: python

    url(r'^', include('yasp.urls', namespace='yasp')),

Add to middlewares:

.. code-block:: python

    MIDDLEWARE_CLASSES = [
        ...
        'yasp.middleware.StaticPageFallbackMiddleware',
    ]


Features
--------

Link to static pages
====================

Static pages in **yasp** are automatically routed to a slug that you specify when
creating your page. Your static pages can be grouped in a `Menu`_ object. So
your urls can be in the form ``menu-slug/page-slug`` or ``page-slug`` (pages
without a relation to `Menu`_).

To create links to static pages there are useful templatetags, as follows.

.. note::

    All menus/pages that are used in a templatetag will be automatically
    created if they don't exist.


To load all pages inside a menu:

.. code-block:: django

    {% load yasp %}

    {% get_pages_from_menu 'about-us' as pages %}

    <ul>
      {% for page in pages %}
        <li><a href="{{page.get_absolute_url}}">{{page.title}}</a></li>
      {% endfor %}
    </ul>


To get a specific page:

.. code-block:: django

    {% load yasp %}

    {% get_page 'about-us/vision' as page %} {# Page 'vision' related to a menu 'about-us' #}
    <a href="{{page.get_absolute_url}}">{{page.title}}</a>

    {% get_page 'contact' as page %} {# Page without a menu. #}
    <a href="{{page.get_absolute_url}}">{{page.title}}</a>

To get a URL to a specific page:

.. code-block:: django

    {% load yasp %}

    <a href="{% get_page_url 'about-us/vision' %}">Our vision</a>


Custom templates
================

Static pages will be rendered using the ``yasp/default.html`` template by
default.

You can customize the template used to render a page by placing a template with
the same slug of the page, or directly on the ``template`` field on Admin.

Template path resolution order:

* The path in the ``template`` field of your page, if provided.
* ``yasp/{menu_slug}/{page_slug}.html``
* ``yasp/{page_slug}.html``
* ``yasp/default.html``


Context of a static page template:

:menu:  The `Menu`_ object.
:content: The `FlatPage`_ object.
:object: Alias to `content`.


External link
=============

You can use a static page instance to link to an external page.

Example:

.. code-block:: python

    >>> from yasp.models import Menu, FlatPage
    >>> menu = Menu.objects.create(name='About us', slug='about-us')
    >>> page = FlatPage.objects.create(menu=menu, slug='google', link='http://google.com', title='Google')
    >>> '<a href="{}">{}</a>'.format(page.get_absolute_url(), page.title)
    '<a href="http://google.com">Google Inc.</a>'

    >>> vision = FlatPage.objects.create(menu=menu, slug='vision', title='Vision')
    >>> '<a href="{}">{}</a>'.format(vision.get_absolute_url(), vision.title)
    '<a href="/about-us/vision">Vision</a>'

This construction is can be specially useful when you're build a navbar in
templates:

.. code-block:: django

    {% load yasp %}
    {% get_pages_from_menu 'about-us' as pages %}

    <ul>
      {% for page in pages %}
        <li><a href="{{page.get_absolute_url}}">{{page.title}}</a></li>
      {% endfor %}
    </ul>


Will render as:

.. code-block:: html

    <ul>
        <li><a href="http://google.com">Google</a></li>
        <li><a href="/about-us/vision">Vision</a></li>
    </ul>



Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements_test.txt
    (myenv) $ py.test
