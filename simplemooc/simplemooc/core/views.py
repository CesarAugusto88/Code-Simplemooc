from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	# return HttpResponse('Hello World!')
	# Usando render
	return render(request, 'home.html')


def contact(request):
	return render(request, 'contact.html')