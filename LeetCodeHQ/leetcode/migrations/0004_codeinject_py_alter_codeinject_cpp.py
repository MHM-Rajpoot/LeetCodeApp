# Generated by Django 5.1.3 on 2024-11-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leetcode', '0003_rename_text_codeinject_cpp'),
    ]

    operations = [
        migrations.AddField(
            model_name='codeinject',
            name='py',
            field=models.TextField(max_length=13000, null=True),
        ),
        migrations.AlterField(
            model_name='codeinject',
            name='cpp',
            field=models.TextField(max_length=13000, null=True),
        ),
    ]
