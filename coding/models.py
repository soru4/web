from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Code(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)

class Choices(models.Model):
    choiceText = models.TextField((""))
    correct = models.TextField((""))

class Questions(models.Model):
    questionTitle = models.TextField()
    questionChoices = models.ManyToManyField(Choices, verbose_name=(""))

class PracticeTest(models.Model):
    testName = models.TextField()
    questions = models.ManyToManyField(Questions, verbose_name=(""))