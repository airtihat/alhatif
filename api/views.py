from django.shortcuts import render, redirect
from .forms import APIRequestForm
from .models import APIRequest

def request_list(request):
    requests = APIRequest.objects.all()
    return render(request, 'api/request_list.html', {'requests': requests})

def create_request(request):
    if request.method == 'POST':
        form = APIRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('api:request_list')
    else:
        form = APIRequestForm()
    return render(request, 'api/create_request.html', {'form': form})
