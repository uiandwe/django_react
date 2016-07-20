# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-20 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
