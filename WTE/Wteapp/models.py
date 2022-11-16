from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class restaurant(models.Model):
    picture = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length=2048)
    city = models.TextField()
    address = models.TextField()
    cuisine = models.TextField()
    description = models.TextField()
    work_time = models.TextField()
    menu = models.URLField()
    location = models.URLField()
    rating = models.FloatField()


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(restaurant, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField()

class cafe(models.Model):
    picture = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length=2048)
    city = models.TextField()
    address = models.TextField()
    cuisine = models.TextField()
    description = models.TextField()
    work_time = models.TextField()
    menu = models.URLField()
    location = models.URLField()
    rating = models.FloatField()

class CommentCafes(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    post = models.ForeignKey(cafe, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField()
