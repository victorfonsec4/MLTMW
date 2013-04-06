from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render

def home(request):
	return render(request, 'mysite/home.html')