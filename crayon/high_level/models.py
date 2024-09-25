# election/models.py
from django.db import models

class Local(models.Model):
  nom = models.CharField(max_length=100)
  ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
  surface = models.IntegerField()
  class Meta:
    abstract = True
