# Generated by Django 2.2 on 2019-06-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0009_task_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]