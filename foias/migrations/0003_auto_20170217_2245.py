# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foias', '0002_auto_20170217_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foia',
            name='ack_date',
            field=models.DateField(blank=True, verbose_name='date acknowledgement letter received'),
        ),
        migrations.AlterField(
            model_name='foia',
            name='appeal_date',
            field=models.DateField(blank=True, verbose_name='date appeal filed'),
        ),
        migrations.AlterField(
            model_name='foia',
            name='request_number',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='foia',
            name='resp_date',
            field=models.DateField(blank=True, verbose_name='date response received'),
        ),
        migrations.AlterField(
            model_name='foia',
            name='response_notes',
            field=models.TextField(blank=True, verbose_name='Notes about your response. (complain about redactions here!) '),
        ),
        migrations.AlterField(
            model_name='foia',
            name='response_url',
            field=models.TextField(blank=True, verbose_name='URL of docs (if they were given to you via a web link)'),
        ),
        migrations.AlterField(
            model_name='foia',
            name='submission_notes',
            field=models.TextField(blank=True, verbose_name="notes about submission (did you send by mail or email? did they tell you what track it's on?)"),
        ),
    ]
