""" Properties URLs. """

# Django
from django.urls import path

# Views
from properties import views

urlpatterns = [
    path(
        route='register/',
        view=views.RegisterProperties.as_view(),
        name='register_properties'
    )
]
