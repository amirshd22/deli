from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=255 ,null=True , blank=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255 ,null=True , blank=True)
    def __str__(self):
        return self.name


class OnlineClass(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    name= models.CharField(max_length=255 ,null=True , blank=True)
    subject= models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    price=models.DecimalField(max_digits=7, decimal_places=0, null=True,blank=True)
    image= models.ImageField(null=True,blank=True)
    createdAt= models.DateTimeField(auto_now_add=True)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    numReviews= models.IntegerField(null=True, blank=True, default=0)
    isAvailable = models.BooleanField(default=False,null=True,blank=True)
    hasOff = models.CharField(max_length=200,null=True,blank=True)
    rating= models.DecimalField(max_digits=7, decimal_places=2, null=True,blank=True)
    students= models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name 


class OnlineClassItems(models.Model):
    onlineClass= models.ForeignKey(OnlineClass, on_delete=models.CASCADE, null=True, blank=True)
    id= models.UUIDField(default=uuid.uuid4,  unique=True, primary_key=True, editable=False)
    title= models.CharField(max_length=255 ,null=True , blank=True)
    description= models.TextField(null=True , blank=True)
    file= models.FileField(null=True,blank=True)
    image= models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.title


class Comments(models.Model):
    video= models.ForeignKey(OnlineClassItems, on_delete=models.SET_NULL,null=True)
    user= models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name= models.CharField(max_length=200 , null=True,blank=True)
    rating= models.IntegerField(null=True, blank=True, default=0)
    comment= models.TextField(null=True, blank=True)
    _id= models.AutoField(primary_key=True, editable=False)
    createdAt= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.rating}-{self.name}")

class Reviews(models.Model):
    onlineclass= models.ForeignKey(OnlineClass, on_delete=models.SET_NULL,null=True)
    user= models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name= models.CharField(max_length=200 , null=True,blank=True)
    rating= models.IntegerField(null=True, blank=True, default=0)
    comment= models.TextField(null=True, blank=True)
    _id= models.AutoField(primary_key=True, editable=False)
    createdAt= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.rating}-{self.name}")