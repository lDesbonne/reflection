# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchQuery',
            fields=[
                ('study_title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('num_docs', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('word', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('cFem', models.IntegerField(default=0)),
                ('cMale', models.IntegerField(default=0)),
            ],
        ),
    ]
