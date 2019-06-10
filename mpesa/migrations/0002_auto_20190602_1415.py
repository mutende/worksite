# Generated by Django 2.2 on 2019-06-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lnmonline',
            name='Amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Checkout_Request_ID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Merchant_Request_ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Mpesa_Receipt_Number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Phone_Number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Result_Code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Result_Description',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='lnmonline',
            name='Transaction_Date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]