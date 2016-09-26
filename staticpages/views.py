from django.shortcuts import render, get_object_or_404

from .models import Menu, FlatPage


def page(request, menu_slug, page_slug):
    menu = get_object_or_404(Menu, slug=menu_slug)
    content = get_object_or_404(FlatPage, menu=menu, slug=page_slug)

    templates = [
        'staticpages/{}/{}.html'.format(menu_slug, page_slug),
        'staticpages/default.html',
    ]
    if content.template_name:
        templates.insert(0, content.template_name)

    context = {
        'menu': menu,
        'object': content,
        'content': content,
    }
    return render(request, templates, context)
