# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 04:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0007_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='entries', to='entries.Entry'),
        ),
    ]