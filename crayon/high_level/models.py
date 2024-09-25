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
