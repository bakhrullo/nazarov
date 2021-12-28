# Generated by Django 4.0 on 2021-12-28 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0009_alter_amapage_nomi'),
    ]

    operations = [
        migrations.CreateModel(
            name='KonfPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Konfiresnsiya',
            },
        ),
        migrations.CreateModel(
            name='LabPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Labaratoriya',
            },
        ),
        migrations.CreateModel(
            name='MusPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Mustaqil talim',
            },
        ),
        migrations.CreateModel(
            name='OakPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'OAK',
            },
        ),
        migrations.CreateModel(
            name='ScopPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Scopsus',
            },
        ),
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
        migrations.AddField(
            model_name='konfirensiya',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.konfpage'),
        ),
        migrations.AddField(
            model_name='labartoriya',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.labpage'),
        ),
        migrations.AddField(
            model_name='mustaqiltalim',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.muspage'),
        ),
        migrations.AddField(
            model_name='oak',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.oakpage'),
        ),
        migrations.AddField(
            model_name='scopus',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.scoppage'),
        ),
    ]
