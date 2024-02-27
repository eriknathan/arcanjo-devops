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
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    # Retorna o nome do contato dentro de contacts no admin do django
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    