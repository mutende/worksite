# Generated by Django 2.2 on 2019-06-20 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_task_complete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='complete',
        ),
    ]