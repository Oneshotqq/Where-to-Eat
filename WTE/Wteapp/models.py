from django.db import models



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