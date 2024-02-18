from django.db import models

# Create your models here.
class Code(models.Model):
    text = models.TextField()

class PracticeTest(models.Model):
    testName = models.TextField()
    qu

class Questions(models.Model):
    