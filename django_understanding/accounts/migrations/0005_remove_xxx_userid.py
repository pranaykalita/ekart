# Generated by Django 4.1.6 on 2023-02-25 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_accountdata_xxx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xxx',
            name='userid',
        ),
    ]
