from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=30)

    # Retorna o nome da categoria dentro de category no admin do django
    def __str__(self) -> str:
        return f'{self.name}'


class Status(models.Model):
    class Meta:
        verbose_name = 'Statu'
        verbose_name_plural = 'Status'

    name = models.CharField(max_length=10)

    # Retorna o nome da categoria dentro de category no admin do django
    def __str__(self) -> str:
        return f'{self.name}'


class Ambiente(models.Model):
    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'

    name = models.CharField(max_length=20)

    # Retorna o nome da categoria dentro de category no admin do django
    def __str__(self) -> str:
        return f'{self.name}'


class ServidorName(models.Model):
    class Meta:
        verbose_name = 'Nome do Servidor'
        verbose_name_plural = 'Nomes do Servidores'

    name = models.CharField(max_length=30)

    # Retorna o nome da categoria dentro de category no admin do django
    def __str__(self) -> str:
        return f'{self.name}'


class ServidorIp(models.Model):
    class Meta:
        verbose_name = 'IP do Servidor'
        verbose_name_plural = 'IPs do Servidor'

    name = models.CharField(max_length=30)

    # Retorna o nome da categoria dentro de category no admin do django
    def __str__(self) -> str:
        return f'{self.name}'


class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, blank=True, null=True)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.SET_NULL, blank=True, null=True)
    technology = models.CharField(max_length=50)
    database = models.CharField(max_length=50)
    project_url = models.URLField(blank=True, null=True)
    server_name = models.ForeignKey(ServidorName, on_delete=models.SET_NULL, blank=True, null=True)
    server_ip = models.ForeignKey(ServidorIp, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.project_name
