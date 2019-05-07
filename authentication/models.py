from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_freelancer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    phoneNumber = models.CharField(max_length=100)
    Address = models.CharField(max_length=100, default="Kenya")
    EducationLevel = models.CharField(max_length=100, null=True, blank=True)
    Skills = models.CharField(max_length=2000,null=True, blank=True)
    Certificate = models.FileField(upload_to='certificates/', max_length=150, null=True, blank=True)
    is_account_active = models.BooleanField(default=False)