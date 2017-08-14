# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-10 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorapp', '0002_post_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='major',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]