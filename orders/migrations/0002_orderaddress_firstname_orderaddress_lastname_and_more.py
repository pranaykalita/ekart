# Generated by Django 4.2.1 on 2023-05-22 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderaddress',
            name='firstname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='orderaddress',
            name='lastname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderno',
            field=models.CharField(default='ORDER-80E3E014', max_length=255, unique=True),
        ),
    ]
