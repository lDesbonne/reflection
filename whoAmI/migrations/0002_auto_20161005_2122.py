# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoAmI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='cFem',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='word',
            name='cMale',
            field=models.IntegerField(default=1),
        ),
    ]
