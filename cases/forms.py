__author__ = 'leonardogutierrezh'
from django import forms
from cases.models import Case, CaseTrack


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'priority', 'assigned', 'type']


class CaseTrackForm(forms.ModelForm):
    class Meta:
        model = CaseTrack
        fields = ['user_to', 'notes']