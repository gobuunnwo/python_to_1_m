from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home),
    # Views.pyのfirstメソッドにpath(飛ぶ)する
    path('first', views.first), 
    # Views.pyのaboutメソッドに飛ぶ
    path('about', views.about),
    path('contact', views.contact),
    path('lohit', views.lohit),



]
