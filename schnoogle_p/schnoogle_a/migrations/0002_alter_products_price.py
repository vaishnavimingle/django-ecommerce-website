# Generated by Django 4.1.7 on 2023-03-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schnoogle_a', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
