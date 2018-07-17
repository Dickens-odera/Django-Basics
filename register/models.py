from django.db import models
from datetime import datetime
# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length= 20)
    email = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Login"

class Posts(models.Model):
    detail = models.TextField()
    posted_by = models.CharField(max_length=40)
    date_posted = models.DateTimeField(default = datetime.now)
    email_address = models.EmailField()
    def __str__(self):
        return self.detail
    class Meta:
        verbose_name_plural = "Posts"