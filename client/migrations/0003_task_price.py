# Generated by Django 2.2 on 2019-05-21 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_clientcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=7),
            preserve_default=False,
        ),
    ]
