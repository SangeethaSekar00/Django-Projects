from django.db import models
from django.urls import reverse

# Create your models here.
class StudentData(models.Model):

    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    standard = models.IntegerField()
    fatherName = models.CharField(max_length=20)
    fatherContact = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('listStudents')
