# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0003_auto_20170830_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_four_news_portal',
            name='document_file',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='form_three_news_portal',
            name='document_file',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='form_two_news_portal',
            name='document_file',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]