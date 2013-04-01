from django.db import models
import ast
#classe usada pra inserir lista no banco de dados

class Produto(models.Model):
	idn = models.CharField(max_length = 30)
	name = models.CharField(max_length = 300)
	def __unicode__(self):
		return self.name

class Dia(models.Model):
	date = models.DateField()
	vendidos = models.IntegerField()
	total = models.IntegerField()
	taxa = models.DecimalField(max_digits = 4, decimal_places = 3)
	produto = models.ForeignKey(Produto)
	def __unicode__(self):
		return u"%s %s" % (self.date, self.produto)
