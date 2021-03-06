# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 02:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogues', '0026_school_boarding_hod_school_games_hod_school_guiding_and_counseling_hod_school_humanities_hod_school_'),
    ]

    operations = [
        migrations.CreateModel(
            name='School_student_council',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('photo', models.FileField(upload_to='uploads/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='School_teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('photo', models.FileField(upload_to='uploads/')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='school_performance',
            name='total_students',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='school_performance',
            name='university_qualified',
            field=models.IntegerField(default=0),
        ),
    ]
