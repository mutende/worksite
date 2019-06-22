# Generated by Django 2.2 on 2019-06-18 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0031_auto_20190618_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reassigendtask',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='reassigendtask',
            name='revised_file',
        ),
        migrations.CreateModel(
            name='CompletedReassignedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revised_file', models.FileField(blank=True, max_length=255, null=True, upload_to='Tasks/Completed/Reassigned/Revised')),
                ('rating', models.FloatField(blank=True, choices=[(2.0, 'Satisfied'), (1.0, 'Not Satisfied')], null=True)),
                ('reassigned_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freelancer.ReassigendTask')),
            ],
        ),
    ]