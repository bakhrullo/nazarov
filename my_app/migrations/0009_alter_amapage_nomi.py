# Generated by Django 4.0 on 2021-12-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_amapage_alter_amaliyot_options_alter_marpage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amapage',
            name='nomi',
            field=models.CharField(max_length=100),
        ),
    ]
