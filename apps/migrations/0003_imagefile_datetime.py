# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20160816_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefile',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]