# coding: utf-8
from __future__ import unicode_literals

from django import template

from ..models import FlatPage, Menu

register = template.Library()


@register.assignment_tag
def get_pages_from_menu(menu_slug):
    """
    Usage:

        {% load staticpages_tags %}

        {% get_pages_from_menu 'about-us' as about_us_pages %}

        {% for i in about_us_pages %}
            Title: {{i.title}}
            ...
        {% endfor%}
    """

    pages = FlatPage.objects.select_related('menu') \
        .filter(menu__slug=menu_slug)
    if not pages:
        Menu.objects.get_or_create(slug=menu_slug, defaults={'name': menu_slug})
    return pages


@register.assignment_tag
def get_page(slug):
    """
    Usage:

        {% load staticpages_tags %}

        {% get_page 'about-us/vision' as vision %}
        Title: {{vision.title}}
        ...
    """
    slugs = slug.split('/')
    if len(slugs) != 2:
        raise ValueError('Param must be "menu-slug/page-slug. Invalid: {}'.format(slug))

    menu_slug, page_slug = slugs
    page = FlatPage.objects.select_related('menu') \
        .filter(menu__slug=menu_slug, slug=page_slug, ) \
        .first()

    if not page:
        menu, created = Menu.objects.get_or_create(slug=menu_slug, defaults={'name': menu_slug})
        page, created = FlatPage.objects.get_or_create(
            menu=menu,
            slug=page_slug,
            defaults=dict(
                title=page_slug,
            )
        )
    return page


@register.assignment_tag
def get_page_url(slug):
    """
    Usage:

        {% load staticpages_tags %}

        <a href="{% get_page_url 'about-us/vision' %}">Our vision</a>
        ...
    """
    page = get_page(slug)
    return page.get_absolute_url() if page else ''
