from django.http import HttpResponse
from django.template import Context, loader
from polls.models import Produto
from polls.models import Poll
from django.shortcuts import render

def index(request):
	lastest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {'lastest_poll_list' : lastest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request):
	product_name = request.GET.get('productname')
	lista = Produto.objects.filter(name__icontains = product_name)
	resposta = ""
	context = {'lista' : lista}
	return render(request, 'polls/resultados.html', context)
	for produtos in lista:
		resposta += produtos.name + " "
	return HttpResponse(resposta)

def vote(request, poll_id):
	return HttpResponse("You're voting on poll %s." % poll_id)

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll %s" % poll_id)

def contact(request):
	if request.method == 'POST' :
		form = ContactForm(request.POST)
		return HttpResponseRedirect('/thanks/')
	else:
		form = ContactForm()
	return render(request, 'contact.html',{
			'form' : form,
	})

def final(request, poll_id):
	mercadoria = Produto.objects.filter(id = poll_id)
	prod = []
	for i in range(0,2):
		prod.append([mercadoria[0].taxa[i], i])
	context = {'mercadoria' : prod}
	return render(request, 'polls/final.html', context)
	return HttpResponse(mercadoria)
