# Generated by Django 3.2.18 on 2023-05-20 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0017_alter_project_complexity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='licence_pic',
            field=models.FileField(blank=True, null=True, upload_to='licence_pic'),
        ),
    ]
