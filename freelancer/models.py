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
    bidded = models.BooleanField(default=False)
    
    objects = models.Manager()
    def __str__(self):
        return str(self.task)

class Completed(models.Model):
    RATING_CHOICES = (
    (5.0,'Excellent'),
    (4.0,'Good'),
    (3.0,'Average'),
    (2.0,'Weak'),
    (1.0,'Poor'),
    )    
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    file = models.FileField(upload_to='Tasks/Completed', max_length=255, null=False, blank=False)
    description = models.TextField(max_length=500, blank=False, null=False, default='Work Complete')
    rating = models.FloatField(choices=RATING_CHOICES, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    re_assigned = models.BooleanField(default=False)
    #complete_reassigned = models.BooleanField(default=False)
    rated = models.BooleanField(default=False)
    objects = models.Manager()

    
    def __str__(self):
        return str(self.freelancer)
    class Meta:
        verbose_name_plural = 'Completed Tasks'

class ReassigendTask(models.Model):
    RATING_CHOICES = (
    (5.0,'Excellent'),
    (4.0,'Good'),
    (3.0,'Average'),
    (2.0,'Weak'),
    (1.0,'Poor'),
    )
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reassigned_freelancer', null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client', null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, null=True, blank=True)
    reasons = models.CharField(max_length = 255)
    rating = models.FloatField(choices=RATING_CHOICES, blank=True, null=True)
    file = models.FileField(upload_to='Tasks/Completed/Reassigned', max_length=255, null=False, blank=False)
    objects = models.Manager()

class FreelancerAccountSummery(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='freelancer')
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.amount)

    class Meta:
        verbose_name_plural = 'Payment Summery' 


@receiver(post_delete, sender=Completed)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False)


@receiver(post_delete, sender=ReassigendTask)
def submission_delete2(sender, instance, **kwargs):
    instance.file.delete(False)

