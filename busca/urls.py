from django.conf.urls import patterns, url

from busca import views

urlpatterns = patterns('',
	#pagina principal da busca
	url(r'^$', views.index, name = 'index'),
	#pagina que mostra lista de produtos com o nome requerido
	url(r'^product/', views.detail, name = 'detail'),
	#pagina com informacoes sobre o produto escolhido
	url(r'^(?P<poll_id>\d+)/$', views.final, name = 'final'),
	)

