from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='students/')
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.name