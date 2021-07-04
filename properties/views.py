""" Properties views """

# Django
from django.shortcuts import render, redirect
from django.views.generic import FormView

# Models
from properties.models import Properties

# Forms
from properties.forms import FormRegisterProperties

class RegisterProperties(FormView):
    template_name = 'properties/register.html'
    form_class = FormRegisterProperties

    def form_valid(self, form):
        """ Save form data. """
        form.save()
        return super().form_valid(form)
