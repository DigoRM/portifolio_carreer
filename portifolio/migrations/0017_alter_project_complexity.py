# Generated by Django 3.2.18 on 2023-05-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0016_auto_20230515_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='complexity',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Low'), (2, 'Regular'), (4, 'High'), (10, 'Professional')], null=True),
        ),
    ]
