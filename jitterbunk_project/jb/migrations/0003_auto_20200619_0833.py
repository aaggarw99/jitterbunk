# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-06-19 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jb', '0002_auto_20200618_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bunk_received', to='jb.UserProfile'),
        ),
        migrations.AlterField(
            model_name='bunk',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, verbose_name='bunking date'),
        ),
        migrations.AlterField(
            model_name='bunk',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bunk_sent', to='jb.UserProfile'),
        ),
    ]
