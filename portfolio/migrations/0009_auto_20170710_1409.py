# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-10 21:09
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20161230_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='/static/portfolio/images'),
        ),
    ]
