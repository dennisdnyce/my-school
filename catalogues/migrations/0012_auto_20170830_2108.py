# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0011_school_performance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_performance',
            name='school_mean_score',
            field=models.FloatField(default=0),
        ),
    ]