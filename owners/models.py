""" Owners model. """

# Django
from django.db import models

# Utilities
from utils.models import BasicModel

class Owner(BasicModel):
    """ Owner models. """
    name = models.CharField(max_length=200)
    person_type = models.CharField(max_length=20, blank=False)
    personal_idendification_number = models.CharField(max_length=20, primary_key=True)

    class Meta(BasicModel.Meta):
        db_table = "owners"
