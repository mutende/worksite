from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from worksiteadmin.models import SkillSet,EducationLevelSet
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    is_freelancer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=100, default="Kenya")
    best_skill = models.ForeignKey(SkillSet, on_delete=models.SET_NULL, null= True, blank = True)
    highest_education_level = models.ForeignKey(EducationLevelSet, on_delete=models.SET_NULL, null= True, blank = True)
    certificate = models.FileField(upload_to='Certificates/', max_length=150, null=True, blank=True)
    is_account_active = models.BooleanField(default=False)


@receiver(post_delete, sender=User)
def submission_delete(sender, instance, **kwargs):
    instance.certificate.delete(False) 

