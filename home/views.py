""" Class Based Views """

from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView, ListView, FormView

from .forms import ContactForm
from .models import Project, Portfolio
from .utils import send_contact_email


# Create your views here.


class HomeView(TemplateView):
    """ Home view class """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        portfolio = get_object_or_404(Portfolio, pk=1)
        context['title'] = "Home"
        context['resume'] = portfolio.resume
        context['github'] = portfolio.github_link
        context['linkedin'] = portfolio.linkedin_link
        return context


class ProjectView(ListView):
    """ List of projects """
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'
    paginate_by = 3

    @method_decorator(cache_page(60 * 15))  # cache for 15 minutes
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "All Projects"
        return context


class ContactView(FormView):
    """ Form view for creating a contact"""
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home:contact')

    def form_valid(self, form):
        contact = form.save()
        send_contact_email(contact)
        messages.success(self.request, 'Your message has been sent. Thank you!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Connect with Me!"
        return context
