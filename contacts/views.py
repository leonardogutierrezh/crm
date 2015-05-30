from django.shortcuts import render
from django.views import generic
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy

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
        url = '/case/create/' + str(self.object.pk)
        return url

class CreateSingleContact(generic.CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "create_contact.html"
    success_url = "/contact/list_single/"

class ViewContact(generic.DetailView):
    model = Contact
    template_name = "view_contact.html"

class ListContact(generic.ListView):
    model = Contact
    template_name = 'list_contact.html'
    template_name_suffix = 'contact_list'

class ListContactList(generic.ListView):
    model = Contact
    template_name = 'list_contact_list.html'
    template_name_suffix = 'contact_list'

class EditContact(generic.UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'create_contact.html'
    success_url = reverse_lazy('list_contact_list')


def delete_contact(request, pk):
    print request.user.is_superuser
    if request.user.is_superuser:
        contact = Contact.objects.get(pk=pk)
        name = contact.person
        contact.delete()
        messages.add_message(request, messages.INFO, 'El contacto ' + name + ' ha sido borrado sactisfactoriamente', extra_tags='success')
        return HttpResponseRedirect(reverse('list_contact_list'))
    else:
        messages.add_message(request, messages.INFO, 'Permiso Denegado!', extra_tags='success')
        return HttpResponseRedirect(reverse('list_contact_list'))