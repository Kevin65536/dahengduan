from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('typography/', views.typography, name='typography'),
]
