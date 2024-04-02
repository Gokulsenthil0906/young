from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    organization = models.TextField()
    phone = models.IntegerField()
    option = models.CharField(max_length=255, choices=[("Software service", "Software service"),("Business Intelligence", "Business Intelligence"),("Application Maintenance And Support", "Application Maintenance And Support")])
