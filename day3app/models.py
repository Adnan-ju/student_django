from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    email=models.EmailField(blank=True)
    summary=models.TextField()

    def __str__(self):
        return self.name + ' Author ' + self.author