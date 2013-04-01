from django.http import HttpResponse
from django.template import Context, loader
from busca.models import Produto
from django.shortcuts import render

def index(request):
	return render(request, 'busca/index.html')

def detail(request):
	product_name = request.GET.get('productname')
	lista = Produto.objects.filter(name__icontains = product_name)
	context = {'lista' : lista}
	return render(request, 'busca/resultados.html', context)

def final(request, poll_id):
	produto = Produto.objects.filter(id = poll_id)
	context = {'produtos' : produto}
	return render(request, 'busca/final.html', context)
