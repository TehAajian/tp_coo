# election/models.py
from django.db import models

models.IntegerField()
models.CharField(max_length=100)
models.ManyToManyField(Machine)

models.ForeignKey(
Departement, # ou "self",
on_delete=models.PROTECT,
# blank=True, null=True,
# related_name="+",
)

class Local(models.Model):
  nom = models.CharField(max_length=100)
  ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
  surface = models.IntegerField()
  
class Meta:
  abstract = True
