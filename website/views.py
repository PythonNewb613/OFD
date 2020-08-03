from django.shortcuts import render
from django.core.mail import send_mail
from dental import settings


# English pages
def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def community(request):
    return render(request, 'community.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def covid(request):
    return render(request, 'covid.html', {})


# French pages
def home_fr(request):
    return render(request, 'home_fr.html', {})

def about_fr(request):
    return render(request, 'about_fr.html', {})

def services_fr(request):
    return render(request, 'services_fr.html', {})

def community_fr(request):
    return render(request, 'community_fr.html', {})

def contact_fr(request):
    return render(request, 'contact_fr.html', {})

def covid_fr(request):
    return render(request, 'covid_fr.html', {})
