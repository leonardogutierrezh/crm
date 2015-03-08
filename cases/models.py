from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Case(models.Model):
    c_type = (('Presupuesto', 'pr'), ('instalacion', 'in'))
    title = models.CharField(max_length=500, verbose_name='Titulo')
    type = models.CharField(max_length=30, choices=c_type, verbose_name='Tipo')
    description = models.TextField(max_length=5000, verbose_name='Descripcion')
    date = models.DateTimeField(auto_created=True)


class CaseTrack(models.Model):
    date = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(User)
    notes = models.TextField(max_length=5000)
    case = models.ForeignKey(Case)

class Reminder(models.Model):
    date = models.DateTimeField()
    notes = models.TextField(max_length=500)
    case = models.ForeignKey(Case)
    done = models.BooleanField(default=False)
