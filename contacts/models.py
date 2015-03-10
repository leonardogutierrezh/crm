from django.db import models

# Create your models here.
class Contact(models.Model):
    c_country = (
        ('Venezuela', 'Venezuela'),
        ('Colombia', 'Colombia'),
    )
    c_type = (
        ('Cliente Final', 'Cliente Final'),
        ('Instalador/Integrador', 'Instalador/Integrador'),
        ('Empresa de Vigilancia', 'Empresa de Vigilancia'),
        ('Gerencia de seguridad', 'Gerencia de seguridad'),
        ('Datacard / ID', 'Datacard / ID'),
    )
    c_origin = (
        ('Referido', 'Referido'),
        ('Mercadolibre', 'Mercadolibre'),
        ('Web', 'Web'),
        ('Feria', 'Feria'),
        ('Otro', 'Otro'),
    )
    c_document_type = (
        ('Cedula', 'Cedula'),
        ('Rif', 'Rif'),
    )
    country = models.CharField(max_length=30, verbose_name='Pais', choices=c_country)
    company = models.CharField(max_length=200, verbose_name='Compania', null=True, blank=True)
    person = models.CharField(max_length=200, verbose_name='Persona Contacto')
    rank = models.CharField(max_length=300, verbose_name='Cargo', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Telefono Fijo')
    mobile_phone = models.CharField(max_length=20, verbose_name='Telefono Celular', blank=True, null=True)
    email = models.EmailField()
    type = models.CharField(max_length=100, verbose_name='Tipo de cliente')
    origin = models.CharField(max_length=100, verbose_name='Origen del cliente')
    document_type = models.CharField(max_length=20, verbose_name='Tipo de Documento', choices=c_document_type, blank=True, null=True)
    document = models.CharField(max_length=100, verbose_name='Rif o Cedula', null=True, blank=True)