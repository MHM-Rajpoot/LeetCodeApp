# Generated by Django 5.1.3 on 2024-11-18 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leetcode', '0004_codeinject_py_alter_codeinject_cpp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeinject',
            name='cid',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
