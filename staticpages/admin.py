from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html

try:
    from adminsortable2.admin import SortableAdminMixin
except:
    class SortableAdminMixin(object):
        pass

try:
    from core.admin import EditableTextAreaMixin
except:
    class EditableTextAreaMixin(object):
        # TODO: Configure extra media to enable html editing.
        class Media:
            js = [
                '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
                '/static/admin/js/tinymce_setup.js',
            ]

from .models import Menu, FlatPage


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FlatPage)
class FlatPageAdmin(EditableTextAreaMixin, SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'menu', 'url', 'template_name', 'active', 'created_on', )
    list_filter = ('menu', 'active', )
    ordering = ('ordering', )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content', ]

    def url(self, obj):
        return format_html(
            '<a href="{0}">{0}</a>',
            obj.get_absolute_url(),
        )
