# Generated by Django 2.2 on 2019-06-17 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0027_auto_20190617_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reassigendtask',
            name='freelancer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reassigned_freelancer', to=settings.AUTH_USER_MODEL),
        ),
    ]
