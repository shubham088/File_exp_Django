# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfilesmodel',
            old_name='upload',
            new_name='doc',
        ),
    ]
