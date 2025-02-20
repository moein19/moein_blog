from django.db import models
from bloggers.models import Blogger 
from datetime import datetime

class Post(models.Model):
    blogger = models.ForeignKey(Blogger,on_delete=models.DO_NOTHING)
    post_title = models.CharField()
    post_date = models.DateTimeField(datetime.now,blank=True)
    post_text = models.TextField()
    photo_main = models.ImageField()
    photo_1 = models.ImageField()
    photo_2 = models.ImageField()
    photo_3 = models.ImageField()
    photo_4 = models.ImageField()
    photo_5 = models.ImageField()
    photo_6 = models.ImageField()