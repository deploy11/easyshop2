from .views import *
from django.urls import path

urlpatterns = [
    path('',home2,name='home2'),
    path('serves/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact),
    path('products/<slug>/',products, name='products'),
    path('register/',register),
    path('single/<int:pk>/',single, name='single'),
    path('contact/',contact,name='contact')
]