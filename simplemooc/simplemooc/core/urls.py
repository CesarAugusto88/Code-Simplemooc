from django.contrib import admin 
from django.urls import path, re_path
from .core import urls 
urlpatterns = [
	path('', views.home, name='home'),
	path('contato/', views.contact, name='contact'),

]