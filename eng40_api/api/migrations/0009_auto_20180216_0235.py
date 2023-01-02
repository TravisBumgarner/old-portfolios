# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-16 02:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_link_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='camera',
        ),
        migrations.RemoveField(
            model_name='image',
            name='exposure',
        ),
        migrations.RemoveField(
            model_name='image',
            name='external_src',
        ),
        migrations.RemoveField(
            model_name='link',
            name='link',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_image', to='api.Project'),
        ),
        migrations.AddField(
            model_name='link',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_link', to='api.Project'),
        ),
    ]