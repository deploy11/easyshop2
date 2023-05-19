from django.urls import path
from .views import *
urlpatterns = [
    path('',blogView,name='blog'),
    path('post/<int:pk>/',detailView.as_view(),name='detail'),
]
