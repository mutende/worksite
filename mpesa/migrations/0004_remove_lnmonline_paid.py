# Generated by Django 2.2 on 2019-06-10 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0003_auto_20190603_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lnmonline',
            name='Paid',
        ),
    ]
