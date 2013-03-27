from django.db import models
import ast

class Poll(models.Model):
	question = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	def __unicode__(self):
		return self.question

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.choice_text

class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class Produto(models.Model):
	productId = models.CharField(max_length = 30)
	name = models.CharField(max_length = 300)
	date = ListField()
	taxa = ListField()
	def __unicode__(self):
		return self.name

#class ListaData(models.Model):
	#def 
# Create your models here.
