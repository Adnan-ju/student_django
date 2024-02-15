from django.db import models

# Create your models here.

class Course(models.Model):
    THEORY = 'Theory'
    LAB = 'Lab'
    PROJECT = 'Project'

    COURSE_TYPE_CHOICES = [
        (THEORY, 'Theory'),
        (LAB, 'Lab'),
        (PROJECT, 'Project'),
    ]
    course_id=models.CharField(max_length=15)
    course_name=models.CharField(max_length=40)
    course_credit=models.DecimalField(max_digits=4,decimal_places=1)
    tutorial_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    att_full_marks=models.DecimalField(max_digits=4, decimal_places=2)
    final_full_marks=models.DecimalField(max_digits=4, decimal_places=2)
    course_type = models.CharField(max_length=10, choices=COURSE_TYPE_CHOICES, default = THEORY)

    def __str__(self):
        return self.course_id + ": " + self.course_name

   
