from django.db import models

# Create your models here.

class Contact(models.Model):
    title=models.CharField(max_length=25)
    email=models.CharField(max_length=100)
    text=models.CharField(max_length=250)

    def __str__(self):
        return self.title
