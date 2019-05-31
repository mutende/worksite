# Generated by Django 2.2 on 2019-05-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0017_auto_20190530_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completed',
            name='rating',
            field=models.CharField(blank=True, choices=[('5', 'Excellent'), ('4', 'Good'), ('3', 'Average'), ('2', 'Weak'), ('1', 'Poor')], max_length=5, null=True),
        ),
    ]