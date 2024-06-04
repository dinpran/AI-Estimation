from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('emissions', views.emissions, name='emissions'),
    path('add/', views.add_inputs, name='add_inputs'),
    path('predict/', views.predict_inputs, name='predict_inputs'),
]
