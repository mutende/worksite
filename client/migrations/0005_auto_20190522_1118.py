# Generated by Django 2.2 on 2019-05-22 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20190522_1104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assign',
        ),
        migrations.RemoveField(
            model_name='task',
            name='bidded',
        ),
        migrations.RemoveField(
            model_name='task',
            name='freelancer',
        ),
    ]
