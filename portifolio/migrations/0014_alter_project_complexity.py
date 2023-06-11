# Generated by Django 3.2.18 on 2023-05-15 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0013_auto_20230514_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='complexity',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Low'), (2, 'Regular'), (3, 'High'), (5, 'Professional')], null=True),
        ),
    ]