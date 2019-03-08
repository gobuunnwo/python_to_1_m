from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='hello-home'),
    path('about', views.home, name='hello-about'),
    path('contact', views.contact, name='hello-contact')

]
