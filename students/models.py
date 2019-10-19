from django.db import models

# Create your models here.

class Students(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'
