__author__ = 'leonardogutierrezh'
from django import forms
from cases.models import Case


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'assigned', 'type']