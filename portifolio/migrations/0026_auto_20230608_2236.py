# Generated by Django 3.2.18 on 2023-06-09 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0025_alter_category_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='frameworks',
            field=models.ManyToManyField(blank=True, null=True, related_name='frameworks', to='portifolio.Framework'),
        ),
        migrations.AlterField(
            model_name='project',
            name='programming_languages',
            field=models.ManyToManyField(blank=True, null=True, related_name='programming_languages', to='portifolio.ProgrammingLanguage'),
        ),
    ]
