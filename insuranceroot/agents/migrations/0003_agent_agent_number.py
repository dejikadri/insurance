# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0002_auto_20180813_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agent_number',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
