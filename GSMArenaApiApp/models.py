from django.db import models

class Phone(models.Model):
    name = models.TextField(verbose_name="Nombre")
    model = models.TextField(verbose_name="Modelo")
    price = models.TextField(verbose_name="Precio")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SmartPhones"
