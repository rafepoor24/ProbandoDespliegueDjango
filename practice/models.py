from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name + '-' +self.lastname
    
    