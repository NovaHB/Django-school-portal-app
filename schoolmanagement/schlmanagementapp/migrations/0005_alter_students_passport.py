# Generated by Django 4.0.2 on 2022-09-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schlmanagementapp', '0004_alter_students_passport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='passport',
            field=models.ImageField(blank=True, upload_to='stud_images'),
        ),
    ]
