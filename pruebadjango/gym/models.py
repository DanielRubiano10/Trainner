from django.db import models

# Create your models here.
class Trainner(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    sexo = models.CharField(max_length=50, verbose_name='sexo')
    edad = models.IntegerField(verbose_name='edad')
    peso = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='peso')
    altura = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='altura')
    cintura = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='cintura')
    cuello = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='cuello')
    cadera = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='cadera')
    actividad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='actividad')
    bmr = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='bmr', blank=True)
    imc = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='imc', blank=True)
    indice_cintura = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='indice_cintura', blank=True)
    porcen_graso = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='porcen_graso', blank=True)
    masa_corporal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='masa_corporal', blank=True)
    calorias = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='calorias', blank=True)