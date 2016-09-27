
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


def get_image_field(verbose_name, max_length=250):
    "Try to use FileBrowseField, with ImageField as fallback"
    try:
        from filebrowser.fields import FileBrowseField
        return FileBrowseField(
            verbose_name,
            max_length=max_length,
            directory='flatpages',
            extensions=['.jpg', '.png'],
            blank=True,
            null=True,
        )
    except:
        return models.ImageField(
            verbose_name,
            max_length=max_length,
            upload_to='flatpages/',
            blank=True,
            null=True,
        )


class Menu(models.Model):
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menu')

    def __unicode__(self):
        return self.name


class FlatPageQuerySet(models.QuerySet):

    def published(self):
        return self.filter(active=True).filter(published_on__lte=timezone.now())


class FlatPage(models.Model):
    menu = models.ForeignKey(
        Menu,
        verbose_name=_('menu'),
        related_name='pages',
        blank=True, null=True)
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    teaser = models.TextField(_('teaser'), blank=True)
    content = models.TextField(_('content'), blank=True)
    template_name = models.CharField(
        _('template name'),
        max_length=70,
        blank=True,
        help_text=_(
            "Example: 'yasp/contact_page.html'. If this isn't provided, "
            "the system will use 'yasp/default.html'."
        ),
    )
    image = get_image_field(_('image'))
    link = models.CharField(_('link'), max_length=200, blank=True)

    active = models.BooleanField(_('active'), default=True)
    ordering = models.PositiveIntegerField(_('ordering'), blank=True, default=1)

    updated_on = models.DateTimeField(_('updated on'), auto_now=True)
    created_on = models.DateTimeField(_('created on'), auto_now_add=True)

    objects = FlatPageQuerySet.as_manager()

    class Meta:
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('ordering', )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if self.link:
            return self.link
        if self.menu:
            return reverse('yasp:page', args=[self.menu.slug, self.slug])
        return reverse('yasp:page', args=[self.slug])

    @property
    def description(self):
        return self.teaser
