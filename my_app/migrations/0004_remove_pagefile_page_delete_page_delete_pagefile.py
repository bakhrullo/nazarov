# Generated by Django 4.0 on 2021-12-27 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_page_pagefile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagefile',
            name='page',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='PageFile',
        ),
    ]
