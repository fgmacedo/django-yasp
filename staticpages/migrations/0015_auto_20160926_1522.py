# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-26 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticpages', '0014_auto_20160906_1633'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flatpage',
            options={'ordering': ('ordering',), 'verbose_name': 'p\xe1gina est\xe1tica', 'verbose_name_plural': 'p\xe1ginas est\xe1ticas'},
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='ordering',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='ordena\xe7\xe3o'),
        ),
    ]
