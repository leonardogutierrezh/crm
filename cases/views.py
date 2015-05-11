from django.shortcuts import render
from django.views.generic.edit import ModelFormMixin, BaseUpdateView
from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib import auth

from cases.models import Case, CaseTrack, UserFullName
from cases.forms import CaseForm, CaseTrackForm
from contacts.models import Contact
# Create your views here.

from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

# Create your views here.
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('my_cases'))
    return render_to_response('login.html', {
        },
        context_instance=RequestContext(request))


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    try:
        if user.is_staff:
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('loggedin'))
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')


def loggedin(request):

    if request.user.is_authenticated():
        x = request.user.username
        return render_to_response('base.html', {
            'user': x,
            },
            context_instance=RequestContext(request)
        )
    else:
        return HttpResponseRedirect('/')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


class CreateCase(generic.CreateView):
    model = Case
    form_class = CaseForm
    template_name = 'create_case.html'
    success_url = reverse_lazy('list_case')

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        print self.kwargs['pk']
        self.object = form.save(commit=False)
        self.object.contact = Contact.objects.get(pk=self.kwargs['pk'])
        self.object.status = 'Abierto'
        self.object.save()
        user_full = UserFullName.objects.get(id=self.request.user.id)
        notes = 'Hola tienes un nuevo caso asignado'
        CaseTrack.objects.create(user_from=user_full, user_to=self.object.assigned, notes=notes, case=self.object)
        return super(ModelFormMixin, self).form_valid(form)

class ListCase(generic.ListView):
    model = Case
    template_name = 'list_case.html'
    context_object_name = 'cases'

class ViewCase(generic.DetailView):
    model = Case
    template_name = 'view_case.html'

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response, using the `response_class` for this
        view, with a template rendered with the given context.
        If any keyword arguments are provided, they will be
        passed to the constructor of the response class.
        """

        history = CaseTrack.objects.filter(case__pk=self.kwargs['pk'])
        context['history'] = history
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,

            **response_kwargs
        )

class MyCases(generic.ListView):
    model = CaseTrack
    template_name = 'my_cases.html'

    def get_queryset(self):
        """
        Return the list of items for this view.
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        user_full = UserFullName.objects.get(id=self.request.user.id)
        queryset = CaseTrack.objects.filter(user_to=user_full, done=False)
        return queryset

class SendCase(generic.CreateView):
    model = CaseTrack
    template_name = 'send_case.html'
    form_class = CaseTrackForm
    success_url = reverse_lazy('my_cases')

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response, using the `response_class` for this
        view, with a template rendered with the given context.
        If any keyword arguments are provided, they will be
        passed to the constructor of the response class.
        """

        casetrack = CaseTrack.objects.get(id=self.kwargs['pk'])
        context['casetrack'] = casetrack
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )


    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        old_track = CaseTrack.objects.get(id=self.kwargs['pk'])
        old_track.done = True
        old_track.save()

        print self.kwargs['pk']
        self.object = form.save(commit=False)
        self.object.case = old_track.case
        self.object.user_from = old_track.user_to
        self.object.save()
        old_track.case.assigned = self.object.user_to
        old_track.case.save()


        return super(ModelFormMixin, self).form_valid(form)