# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-26 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yasp', '0016_auto_20160926_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='teaser',
            field=models.TextField(blank=True, verbose_name='teaser'),
        ),
    ]