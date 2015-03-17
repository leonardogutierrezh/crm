# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=500, verbose_name=b'Titulo')),
                ('type', models.CharField(max_length=30, verbose_name=b'Tipo', choices=[(b'Presupuesto', b'Presupuesto'), (b'Instalacion', b'Instalacion')])),
                ('description', models.TextField(max_length=5000, verbose_name=b'Descripcion')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CaseTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_created=True)),
                ('notes_from', models.TextField(max_length=5000)),
                ('notes_to', models.TextField(max_length=5000)),
                ('case', models.ForeignKey(to='cases.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('notes', models.TextField(max_length=500)),
                ('done', models.BooleanField(default=False)),
                ('case', models.ForeignKey(to='cases.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserFullName',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='case',
            name='assigned',
            field=models.ForeignKey(to='cases.UserFullName'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='casetrack',
            name='user_to',
            field=models.ForeignKey(related_name='from', to='cases.UserFullName'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='casetrack',
            name='user_from',
            field=models.ForeignKey(related_name='to', to='cases.UserFullName'),
            preserve_default=True,
        ),
    ]
