# Generated by Django 4.0 on 2021-12-20 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Burgerking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
