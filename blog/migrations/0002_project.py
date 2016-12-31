# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-14 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image_url', models.ImageField(blank=True, upload_to=b'')),
                ('github_url', models.URLField(blank=True)),
                ('demo_url', models.URLField(blank=True)),
            ],
        ),
    ]