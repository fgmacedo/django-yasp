# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staticpages', '0003_auto_20160801_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='teaser',
            field=models.CharField(blank=True, max_length=140, verbose_name='teaser'),
        ),
    ]
