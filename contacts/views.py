from django.shortcuts import render
from django.views import generic
from .models import Contact
from .forms import ContactForm


# Create your views here.
class CreateContact(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "create_contact.html"


    def get_success_url(self):
        """
        Returns the supplied URL.
        """
        print self.object.pk
        url = '/case/create_case/' + str(self.object.pk)
        return url


class ListContact(generic.ListView):
    model = Contact
    template_name = 'list_contact.html'
    template_name_suffix = 'contact_list'