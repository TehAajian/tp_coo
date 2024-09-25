# election/models.py
from django.db import models

class Ville(models.Model):
  nom_Ville = models.CharField(max_length=100)
  code_postal = models.IntegerField()
  prix_m_2 = models.IntegerField()
  def __str__(self):
    return self.nom

class Local(models.Model):
  nom_Local = models.CharField(max_length=100)
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
  machines = models.CharField(max_length=100)
  def __str__(self):
    return self.nom
      
class Machine(Usine):
  nom_Machine = models.CharField(max_length=100)
  prix_Machine = models.IntegerField()
  n_serie = models.IntegerField()
  def __str__(self):
    return self.nom

class Stock(models.Model):
  objet_Stock = models.CharField(max_length=100)
  nombre_Stock = models.IntegerField()
  def __str__(self):
    return self.nom

class Etape(models.Model):
  nom_Etape = models.CharField(max_length=100)
  machine_Etape = models.CharField(max_length=100)
  quantite_ressource = models.IntegerField()
  duree = models.IntegerField()
  etape_suivante = models.CharField(max_length=100)
  def __str__(self):
    return self.nom
    
class QuantiteRessource(models.Model):
  ressource = models.CharField(max_length=100)
  quantite = models.IntegerField()

class Objet(models.Model):
  nom_Objet = models.CharField(max_length=100)
  prix_Objet = models.IntegerField()
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


  
