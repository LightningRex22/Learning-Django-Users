from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Faculty(AbstractUser):
    degrees=[
            ('Bachelors','Bachelors'),
            ('Masters','Masters'),
            ('PhD','PhD'),
            ('Diploma','Diploma'),
        ]
    departments=[
            ('Engineering','Engineering'),
            ('Humanities','Humanities'),
            ('Mathematics','Mathematics'),
            ('MCA','MCA'),
            ('Physics','Physics'),
            ('Chemistry','Chemistry'),
        ]
    degree = models.CharField(max_length=20, choices=degrees, blank=True)
    department = models.CharField(max_length=20, choices=departments, blank=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)