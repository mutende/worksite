# Generated by Django 2.2 on 2019-05-22 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0003_task_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assign',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='bidded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='freelancer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to=settings.AUTH_USER_MODEL),
        ),
    ]
