from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/create_contact.html', {'form': form})
