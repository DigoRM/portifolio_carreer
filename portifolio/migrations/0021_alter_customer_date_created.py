# Generated by Django 3.2.18 on 2023-06-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0020_project_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateField(null=True),
        ),
    ]