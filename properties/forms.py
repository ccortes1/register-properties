""" Properties forms """

# Django
from django import forms

# Models
from properties.models import Properties

PROPERTY_TYPE_CHOICES = [
    ('rural', 'Rural'),
    ('urbano', 'Urbano'),
]

class FormRegisterProperties(forms.Form):
    """ Form register properties """
    cedula_catastral = forms.CharField(max_length=40)
    address_or_name_properties = forms.CharField(max_length=100)
    property_type = forms.ChoiceField(widget=forms.Select, choices=PROPERTY_TYPE_CHOICES,)
    real_estate_registration_number = forms.CharField(max_length=16)
    owners = forms.CharField(max_length=20)

    def clean_real_estate_registration_number(self):
        real_estate_registration_number = self.cleaned_data['real_estate_registration_number']
        real_estate_registration_number_taken = Properties.objects.filter(real_estate_registration_number=real_estate_registration_number).exists()
        if real_estate_registration_number_taken:
            raise forms.VallidationError('Personal identification number already exist in the system')
        return real_estate_registration_number

    def save(self):
        """Created property"""
        data = self.clean_real_estate_registration_number
        properties = Properties(data)
        properties.save()


