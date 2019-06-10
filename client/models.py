from django.db import models
from authentication.models import User
from worksiteadmin.models import SkillSet,EducationLevelSet
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class Task(models.Model):
    FORMAT_AS_CHOICES = (
    ('None','None'),
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
    documet_format = models.CharField(max_length=100,choices=FORMAT_AS_CHOICES, default='None')
    task_file = models.FileField(upload_to='Tasks/', max_length=150, null=True, blank=True)
    price = models.FloatField()
    is_taken = models.BooleanField(default=False)
    show = models.BooleanField(default=True)
    paid = models.BooleanField(default=False)
    
    

    objects = models.Manager()

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Task)
def submission_delete(sender, instance, **kwargs):
    instance.task_file.delete(False)


class ClientComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    comment_date = models.DateField(auto_now_add=True)

    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Read Comments'

