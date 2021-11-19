from django.db import models
from userapp.models import SignUp
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(SignUp, on_delete=models.CASCADE)
    publish = models.DateTimeField(auto_now_add=True, auto_created=True)
    image = models.ImageField(blank=True, upload_to='media/uploaded')
    status = models.CharField(max_length=500, default="UnApproved", blank=False)

    # status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
