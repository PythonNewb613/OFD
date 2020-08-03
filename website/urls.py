from django.urls import path
from . import views


urlpatterns = [
    path('',                  views.home,         name="home"),
    path('about.html',        views.about,        name="about"),
    path('services.html',     views.services,     name="services"),
    path('community.html',    views.community,    name="community"),
    path('contact.html',      views.contact,      name="contact"),
    path('covid.html',        views.covid,        name="covid"),
    path('home_fr.html',      views.home_fr,      name="home_fr"),
    path('about_fr.html',     views.about_fr,     name="about_fr"),
    path('services_fr.html',  views.services_fr,  name="services_fr"),
    path('community_fr.html', views.community_fr, name="community_fr"),
    path('contact_fr.html',   views.contact_fr,   name="contact_fr"),
    path('covid_fr.html',     views.covid_fr,     name="covid_fr"),
]