# Generated by Django 4.1.7 on 2023-03-13 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ecom_seller',
            fields=[
                ('seller_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('seller_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
