from django.db import models

class Blogger(models.Model):
    name = models.CharField(max_length=200)
    user_name = models.CharField()
    email = models.EmailField()
    photo = models.ImageField()
    description = models.TextField()