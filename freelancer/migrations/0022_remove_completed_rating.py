# Generated by Django 2.2 on 2019-06-08 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0021_bid_bidded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completed',
            name='rating',
        ),
    ]
