from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Menu, FlatPage


def _normalize_slugs(menu_slug, page_slug, url):
    if not (menu_slug or page_slug) and url:
        if url.startswith('/'):
            url = url[1:]
        if url.endswith('/'):
            url = url[:-1]
        parts = url.split('/')
        if len(parts) == 1:
            menu_slug = None
            page_slug = parts[0]
        elif len(parts) == 2:
            menu_slug, page_slug = parts
        else:
            raise Http404
    return menu_slug, page_slug


def page(request, menu_slug='', page_slug='', url=''):
    menu_slug, page_slug = _normalize_slugs(menu_slug, page_slug, url)

    try:
        menu = get_object_or_404(Menu, slug=menu_slug)
    except:
        menu = None
    content = get_object_or_404(FlatPage, menu=menu, slug=page_slug)

    templates = [
        'yasp/{}/{}.html'.format(menu_slug, page_slug),
        'yasp/{}.html'.format(page_slug),
        'yasp/default.html',
    ]
    if content.template_name:
        templates.insert(0, content.template_name)

    context = {
        'menu': menu,
        'object': content,
        'content': content,
    }
    return render(request, templates, context)
