# Generated by Django 2.2 on 2019-06-18 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0030_auto_20190617_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reassigendtask',
            options={'verbose_name_plural': 'Reassigend Task'},
        ),
        migrations.AddField(
            model_name='reassigendtask',
            name='revised_file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='Tasks/Completed/Reassigned/Revised'),
        ),
    ]