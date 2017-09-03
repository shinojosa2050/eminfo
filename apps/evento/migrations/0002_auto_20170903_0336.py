# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='Codigo',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='Encargado',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
    ]
