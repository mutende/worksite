# Generated by Django 2.2 on 2019-05-30 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('freelancer', '0016_auto_20190530_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completed',
            name='rating',
            field=models.CharField(blank=True, choices=[('5', 'Excellent'), ('4', 'Good'), ('3', 'Average'), ('2', 'Weak'), ('1', 'Poor')], max_length=3, null=True),
        ),
        migrations.CreateModel(
            name='FreelancerAccountSummery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='freelancer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payment Summery',
            },
        ),
    ]