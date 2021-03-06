# Generated by Django 2.2 on 2019-06-18 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0032_auto_20190618_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='completedreassignedtask',
            options={'verbose_name_plural': 'Completed Reassigned Tasks'},
        ),
        migrations.AlterModelOptions(
            name='reassigendtask',
            options={'verbose_name_plural': 'Reassigned Tasks'},
        ),
        migrations.AlterField(
            model_name='completed',
            name='rating',
            field=models.FloatField(blank=True, choices=[(5.0, 'Excellent'), (4.0, 'Good'), (3.0, 'Average'), (2.0, 'Weak'), (1.0, 'Poor'), (0.0, 'Reassigned')], null=True),
        ),
    ]
