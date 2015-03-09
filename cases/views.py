from django.shortcuts import render
from django.views.generic.edit import ModelFormMixin, BaseUpdateView
from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from cases.models import Case
from cases.forms import CaseForm
# Create your views here.


class CreateCase(generic.CreateView):
    model = Case
    form_class = CaseForm
    template_name = 'create_case.html'


class ListCase(generic.ListView):
    model = Case
    template_name = 'list_case.html'
    context_object_name = 'cases'