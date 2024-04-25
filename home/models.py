from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} - {self.email} '