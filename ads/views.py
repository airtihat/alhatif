from django.shortcuts import render, redirect
from .forms import AdCampaignForm
from .models import AdCampaign

def ad_list(request):
    ads = AdCampaign.objects.all()
    return render(request, 'ads/ad_list.html', {'ads': ads})

def create_ad(request):
    if request.method == 'POST':
        form = AdCampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ads:ad_list')
    else:
        form = AdCampaignForm()
    return render(request, 'ads/create_ad.html', {'form': form})
