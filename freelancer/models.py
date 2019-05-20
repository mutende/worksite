from django.db import models
from authentication.models import User

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    comment_date = models.DateField(auto_now_add=True)

    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Read Comments'
