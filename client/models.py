from django.db import models
from authentication.models import User
from worksiteadmin.models import SkillSet,EducationLevelSet

# Create your models here.

class Task(models.Model):
    FORMAT_AS_CHOICES = (
    ('APA','APA'),
    ('MLA','MLA'),
    ('Chicago','Chicago'),
    ('Havard','Havard'),
    )
    # clients = models.ManyToManyField(User)
    client= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    best_skill = models.ForeignKey(SkillSet, on_delete=models.SET_NULL, null= True)
    highest_education_level = models.ForeignKey(EducationLevelSet, on_delete=models.SET_NULL, null= True)
    date_posted = models.DateField(auto_now=True)
    expiry_date = models.DateField(auto_now = False)
    documet_format = models.CharField(max_length=100,choices=FORMAT_AS_CHOICES, default='APA')
    task_file = models.FileField(upload_to='Tasks/', max_length=150, null=True, blank=True)
    is_taken = models.BooleanField(default=False)
