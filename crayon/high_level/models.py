# election/models.py
from django.db import models
class Election(models.Model):
title = models.CharField(max_length=200)
pub_date = models.DateTimeField()
class Candidate(models.Model):
election = models.ForeignKey(
Election,
on_delete=models.CASCADE,
)
name = models.CharField(max_length=200)
votes = models.IntegerField(default=0)

class Local(models.model):
  nom = models.CharField(max_length=100)
  ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
  surface = models.IntegerField()

class Meta:
  abstract = True

models.ForeignKey(
Departement, # ou "self",
on_delete=models.PROTECT,
# blank=True, null=True,
# related_name="+",
)
