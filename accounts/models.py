from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):

    ROLE_CHOICES = (
    ('admin','Admin'),
    ('teacher','Teacher'),
    ('student','Student')
    )

    role = models.CharField(
        max_length=25,
        choices=ROLE_CHOICES,
        default='student'
    )



    phone_number = models.CharField(max_length=13)
    birth_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.username

