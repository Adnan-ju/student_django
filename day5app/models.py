from django.conf import settings
from django.db import models
from day4app.models import Course
# Create your models here.

class Student(models.Model):
    std_id = models.IntegerField(primary_key=True)
    std_name = models.CharField(max_length=50)
    std_enrolled_courses = models.ManyToManyField(Course)
    def __str__(self):
        return str(self.std_id) + ":" + self.std_name