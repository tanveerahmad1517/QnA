# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0009_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.TextField(blank=True),
        ),
    ]
