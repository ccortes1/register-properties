""" Owners URLs. """

# Django
from django.urls import path

# Views
from owners import views

urlpatterns = [
    path(
        route='register/',
        view=views.RegisterOwner.as_view(),
        name='register_owner'
    )
]