# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20171025_0659'),
    ]

    operations = [
        migrations.CreateModel(
            name='carareanum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalnum', models.IntegerField()),
                ('remainingnum', models.IntegerField()),
            ],
        ),
    ]
