# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0002_answer_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ans_count',
            field=models.IntegerField(default=0),
        ),
    ]
