__author__ = 'leonardogutierrezh'
from django.contrib import admin
from cases.models import Case, CaseTrack, Reminder

admin.site.register(Case)
admin.site.register(CaseTrack)
admin.site.register(Reminder)