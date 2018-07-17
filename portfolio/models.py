from django.db import models
from datetime import datetime
# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 50)
    reg_number = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(default = datetime.now, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Students"
        