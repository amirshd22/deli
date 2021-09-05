from django.db import models
from django.contrib.auth.models import User
from onlineclass.models import OnlineClass
import uuid
# Create your models here.

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    picture =  models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.user

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    picture =  models.ImageField(null=True, blank=True)
    onlineClasses = models.ManyToManyField(OnlineClass, blank=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)

    def __str__(self):
            return self.user.username