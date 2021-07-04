""" Owners forms """

# Django
from django import forms

# Models
from owners.models import Owner

PERSON_TYPE_CHOICES = [
    ('persona natural', 'Persona natural'),
    ('persona jurídica', 'Persona jurídica'),
]

class FormRegisterOwner(forms.ModelForm):
    """ Form register owner """
    
    class Meta:
        model = Owner
        fields = ('name', 'person_type', 'personal_idendification_number')
        widgets = {
            'person_type': forms.Select(choices=PERSON_TYPE_CHOICES)
        }
    """
    def clean_personal_idendification_number(self):
        personal_idendification_number = self.cleaned_data['personal_idendification_number']
        personal_idendification_number_taken = Owner.objects.filter(personal_idendification_number=personal_idendification_number).exists()
        if personal_idendification_number_taken:
            raise forms.ValidationError('Personal identification number already exist in the system')
        return personal_idendification_number

    def save(self):
        data = self.clean_personal_idendification_number
        owner = super().save()
        return owner.save()
    """