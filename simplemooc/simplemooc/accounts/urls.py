from django.urls import path, re_path, include
from django import forms
#from django.contrib.auth.views import LoginView, LogoutView # não funciona
from django.contrib import admin
from . import views

app_name = 'accounts'

urlpatterns = [
	# 'simplemooc.accounts.views.dashboard'
	path('', views.dashboard, name='dashboard'),
	# com mensagem diferente -> include('django.contrib.auth.urls')
    #path('entrar/', LoginView.dispatch, {'template_name': 'accounts/login.html'}, name='login'),
	#path('sair/', LogoutView.dispatch, {'next_page': 'core:home'}, name='logout'),
	path('entrar/', include('django.contrib.auth.urls'), name='login'), # template login teve que ir para core/template/registration
    path('sair/', include('django.contrib.auth.urls'), name='logout'),

	path('cadastre-se/', views.register, name='register'),
	path('nova-senha/', views.password_reset, name='password_reset'),
	re_path(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name='password_reset_confirm'),
	path('editar/', views.edit, name='edit'),
	path('editar-senha/', views.edit_password, name='edit_password'),

]
