from .models import Cities
from django import forms
from django.core.exceptions import ValidationError


class CityForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter city',
                'class': 'form-control'
            })
        }

    def clean_name(self):
        new_name = self.cleaned_data['name'].lower()
        if Cities.objects.filter(name__iexact=new_name).count():
            raise ValidationError('You cannot track same city more than 1 time')
        return new_name.title()

