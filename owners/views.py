""" Owners views """

# Django
from django.shortcuts import render, redirect
from django.views.generic import CreateView

# Models
from owners.models import Owner

# Forms
from owners.forms import FormRegisterOwner


class RegisterOwner(CreateView):
    model = Owner
    template_name = 'owners/register.html'
    form_class = FormRegisterOwner
    
    def form_valid(self, form):
        """ Save form data. """
        print(form)
        print("esto no esta funcionando")
        form.save()
        return super().form_valid(form)






