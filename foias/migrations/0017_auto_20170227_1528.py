# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foias', '0016_nytemployee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nytemployee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='foias.MyUser'),
        ),
    ]
