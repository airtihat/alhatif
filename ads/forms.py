from django import forms
from .models import AdCampaign

class AdCampaignForm(forms.ModelForm):
    class Meta:
        model = AdCampaign
        fields = '__all__'
