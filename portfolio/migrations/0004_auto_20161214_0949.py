# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-14 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20161214_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='project-images'),
        ),
    ]
