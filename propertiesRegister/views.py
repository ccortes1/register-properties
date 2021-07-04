""" Local views """

# Django
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponseRedirect
from properties.models import Properties

def Home(request):
    search = request.GET.get("buscar")
    properties = Properties.objects.all()

    if search:
        properties = Properties.objects.filter(
            Q(cedula_catastral__icontains=search) |
            Q(address_or_name_properties__icontains = search) |
            Q(owners__personal_idendification_number__icontains=search)
        ).distinct()

    return render(request, 'home.html', {'properties':properties})
