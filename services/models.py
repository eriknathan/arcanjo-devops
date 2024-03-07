from django.db import models


class Project(models.Model):
    CATEGORIAS_CHOICES = (
        ('Back-end', 'Back-end'),
        ('Front-end', 'Front-end'),
        ('Outros', 'Outros'),
    )
    STATUS_CHOICES = (
        ('On', 'On'),
        ('Off', 'Off'),
    )

    project_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    technology = models.CharField(max_length=50)
    database = models.CharField(max_length=50)
    project_url = models.URLField()
    server_name = models.CharField(max_length=50)
    server_ip = models.CharField(max_length=15)

    def __str__(self):
        return self.project_name
