from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserFullName(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()

class Case(models.Model):
    c_type = (
        ('Presupuesto', 'Presupuesto'),
        ('Instalacion', 'Instalacion'),
    )
    title = models.CharField(max_length=500, verbose_name='Titulo')
    type = models.CharField(max_length=30, choices=c_type, verbose_name='Tipo')
    description = models.TextField(max_length=5000, verbose_name='Descripcion')
    date = models.DateTimeField(auto_created=True)
    assigned = models.ForeignKey(UserFullName)


class CaseTrack(models.Model):
    date = models.DateTimeField(auto_created=True)
    user_to = models.ForeignKey(UserFullName, related_name='from')
    user_from = models.ForeignKey(UserFullName, related_name='to')
    notes_from = models.TextField(max_length=5000)
    notes_to = models.TextField(max_length=5000)
    case = models.ForeignKey(Case)


class Reminder(models.Model):
    date = models.DateTimeField()
    notes = models.TextField(max_length=500)
    case = models.ForeignKey(Case)
    done = models.BooleanField(default=False)
