# Generated by Django 4.1.7 on 2023-04-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schnoogle_a', '0005_remove_newsletter_signup_date_feedback_message_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
