# Generated by Django 2.2 on 2019-06-03 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0002_auto_20190602_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lnmonline',
            options={'verbose_name_plural': 'MPESA Transactions'},
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Paid',
            field=models.BooleanField(default=False),
        ),
    ]