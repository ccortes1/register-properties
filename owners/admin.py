""" Owners admin. """

# Django
from django.contrib import admin

# Model
from owners.models import Owner

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    """Owner admin"""
    list_display = ('name', 'person_type', 'personal_idendification_number', 'created', 'modified')
    search_fields = ('personal_idendification_number', 'created', 'modified')