# Generated by Django 4.1.7 on 2023-04-03 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schnoogle_a', '0006_alter_feedback_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
