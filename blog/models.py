from django.db import models
from datetime import datetime
# Create your models here.
class BlogPosts(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default =datetime.now,blank= True)
    post = models.TextField()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "BlogPosts"
