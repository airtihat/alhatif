from django import forms
from .models import APIRequest

class APIRequestForm(forms.ModelForm):
    class Meta:
        model = APIRequest
        fields = '__all__'
