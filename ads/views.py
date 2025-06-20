from django.shortcuts import render, redirect
from .models import AdCampaign
from .forms import AdCampaignForm  # تأكد أن هذا الفورم موجود لديك

# عرض قائمة الإعلانات مع الفلاتر
def ads_list(request):
    ads = AdCampaign.objects.all()

    # فلاتر:
    campaign_type = request.GET.get('type')
    status = request.GET.get('status')

    if campaign_type:
        ads = ads.filter(campaign_type=campaign_type)
    if status:
        ads = ads.filter(status=status)

    return render(request, 'ads/ad_list.html', {'ads': ads})

# إنشاء إعلان جديد
def create_ad(request):
    if request.method == 'POST':
        form = AdCampaignForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            return redirect('ads_list')
    else:
        form = AdCampaignForm()
    return render(request, 'ads/create_ad.html', {'form': form})
