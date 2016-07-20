from django.db import models

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=5000, null=True, blank=True)

