# election/models.py
from django.db import models

class Ville(models.Model):
  nom = models.CharField(max_length=100)
  code_postal = models.IntegerField()
  prix_m_2 = models.IntegerField()
  def __str__(self):
    return self.nom

class Local(models.Model):
  nom = models.CharField(max_length=100)
  Ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
  surface = models.IntegerField()
  class Meta:
    abstract = True
  def __str__(self):
    return self.nom

class SiegeSocial(Local):
  def __str__(self):
    return self.nom

class Usine(Local):
  nom = models.CharField(max_length=100)
  def __str__(self):
    return self.nom
      
class Machine(Usine):
  nom = models.CharField(max_length=100)
  prix = models.IntegerField()
  n_serie = models.IntegerField()
  def __str__(self):
    return self.nom

class Stock(models.Model):
  objet = models.CharField(max_length=100)
  nombre = models.IntegerField()
  def __str__(self):
    return self.nom

class Etape(models.Model):
  nom = models.CharField(max_length=100)
  machine = models.CharField(max_length=100)
  quantite_ressource = models.IntegerField()
  duree = models.IntegerField()
  etape_suivante = models.CharField(max_length=100)
  def __str__(self):
    return self.nom

class Objet(models.Model):
  nom = models.CharField(max_length=100)
  prix = models.IntegerField()
  class Meta:
    abstract = True
  def __str__(self):
    return self.nom

class Ressource(Objet):
  def __str__(self):
    return self.nom

class Produit(Objet):
  def __str__(self):
    return self.nom


  
