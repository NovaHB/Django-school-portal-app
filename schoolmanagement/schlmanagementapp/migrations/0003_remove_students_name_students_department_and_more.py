# Generated by Django 4.0.2 on 2022-09-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schlmanagementapp', '0002_alter_students_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='name',
        ),
        migrations.AddField(
            model_name='students',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='faculty',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='grad_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
