# Generated by Django 3.2.18 on 2023-05-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0009_course_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='role',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
