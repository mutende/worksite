from django.db import models
from authentication.models import User
from client.models import Task
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    comment_date = models.DateField(auto_now_add=True)

    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Read Comments'

class Bid(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    assign = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    show = models.BooleanField(default=True)
    
    objects = models.Manager()
    def __str__(self):
        return self.task

class Completed(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    file = models.FileField(upload_to='Tasks/Completed', max_length=150, null=True, blank=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    rating = models.DecimalField(decimal_places=2, max_digits=3, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    re_assigned = models.BooleanField(default=False)
    

    class Meta:
        verbose_name_plural = 'Completed Tasks'
    
    def __str__(self):
        return self.bid


@receiver(post_delete, sender=Completed)
def submission_delete(sender, instance, **kwargs):
    instance.task_file.delete(False)
