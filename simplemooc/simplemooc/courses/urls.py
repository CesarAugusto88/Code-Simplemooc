from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
	path('', views.index, name='index'),
	#path('(?P<pk>\d+)/', views.details, name='details'),
    path('?P<slug>[\w_-]+/', views.details, name='details'),

]