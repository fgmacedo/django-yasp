from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableAdminMixin

from core.admin import EditableTextAreaMixin
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
