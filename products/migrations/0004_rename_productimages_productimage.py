# Generated by Django 4.2.1 on 2023-05-03 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImages',
            new_name='ProductImage',
        ),
    ]
