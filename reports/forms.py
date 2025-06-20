from django import forms
from .models import Campaign  # حسب التطبيق

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'
