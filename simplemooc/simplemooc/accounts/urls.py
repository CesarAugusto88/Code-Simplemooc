from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('entrar/', views.login, {'template_name': 'accounts/login.html'}, name='login'),
	path('sair/', views.logout, {'next_page': 'core:home'}, name='logout'),
	path('cadastre-se/', views.register, name='register'),
	path('nova-senha/', views.password_reset, name='password_reset'),
	path('confirmar-nova-senha/<int:key>/', views.password_reset_confirm, name='password_reset_confirm'),
	path('editar/', views.edit, name='edit'),
	path('editar-senha/', views.edit_password, name='edit_password'),

]
