# forms.py

from django import forms   # type: ignore
from .models import User
from datetime import datetime



def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove default help texts
        for field_name, field in self.fields.items():
            field.help_text = ""


class ProductionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'address']

    def clean_username(self):
            username = self.cleaned_data['username']
            if not username:
                raise forms.ValidationError("User Name cannot be empty.")
            return username
    
    def clean_password(self):
            password = self.cleaned_data['password']
            if not password:
                raise forms.ValidationError("User Password cannot be empty.")
            return password
    
    def clean_address(self):
            address = self.cleaned_data['address']
            if not address:
                raise forms.ValidationError("Address of the user cannot be empty.")
            return address
    

