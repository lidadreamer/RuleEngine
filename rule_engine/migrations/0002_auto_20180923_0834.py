# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-09-23 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule_engine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rules',
            name='criteria',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Operations',
        ),
    ]
