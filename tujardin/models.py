from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Tipo(models.Model):
    idTipo = models.IntegerField(primary_key=True, verbose_name='Id del tipo de producto')
    nomTipo=models.CharField(max_length=50, verbose_name='Nombre del tipo de producto')

    def str(self): 
        return self.nomTipo

class Producto (models.Model): 
    idprod = models.CharField(primary_key=True, max_length=6, verbose_name='Id')
    nomprod= models.CharField(max_length=20, verbose_name='Nombre')
    precio= models.IntegerField(verbose_name='Precio')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name='Tipo')

    def str(self):
        return self.nomprod

class cliente (models.Model):
    gmail= models.charfield(primary_key=True, verbose_name='Gmail')
    nom= models.CharField(min_length=3, verbose_name='Nombre')

    def str(self):
        return self.gmail 

