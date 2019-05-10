from django.db import models

# Create your models here.

class SkillSet(models.Model):
    skills = models.CharField(max_length=250)

    def __str__(self):
        return self.skills

class EducationLevelSet(models.Model):
    education_levels = models.CharField(max_length=100)

    def __str__(self):
        return self.education_levels
