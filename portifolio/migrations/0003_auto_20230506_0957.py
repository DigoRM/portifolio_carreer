# Generated by Django 3.2.18 on 2023-05-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portifolio', '0002_auto_20230505_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='framework',
            field=models.CharField(default='django', max_length=155),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='programming_language',
            field=models.CharField(default='python', max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='update',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]