from django.db import models

# Create your models here.
from django.db import models


class IHA(models.Model):
    marka = models.CharField(max_length=500)
    model = models.CharField(max_length=500)
    agirlik = models.CharField(max_length=500)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Kategori")

    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.marka + " " + self.model


    class Meta:
        verbose_name=("IHAlar")
        verbose_name_plural = ("IHAlar")


class Category(models.Model):
    name = models.CharField(max_length=500, verbose_name="kategori adi")

    def __str__(self):
        return self.name
    class Meta:
        verbose_name=("Kategoriler")
        verbose_name_plural=("Kategoriler")

