from django.db import models
from django.utils import timezone

# Create your models here.

# Isso seria uma "tabela" chamada Contact
class Contact(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=80)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    