from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} - {self.email} '


class Question(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')
    title = models.CharField(max_length=185)
    slug = models.SlugField(max_length=185)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} asked {self.title[:25]} '

class Answer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answers')
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='answers')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} answered {self.question.title[:25]}'