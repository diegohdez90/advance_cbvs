from django.db import models

# Create your models here.
class School(models.Model):
  name = models.CharField(max_length=128)
  principal = models.CharField(max_length=80)
  location = models.CharField(max_length=64)

  def __str__(self):
    return self.name

class Student(models.Model):
  name = models.CharField(max_length=80)
  age = models.PositiveIntegerField()
  school = models.ForeignKey(School, related_name='students')

  def __str__(self):
    return self.name
