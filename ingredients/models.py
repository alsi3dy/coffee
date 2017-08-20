from django.db import models
from django.contrib.auth.models import User


class Bean(models.Model):

	title = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=7,decimal_places=3)
	description = models.TextField(null=True , blank=True)

	def __str__(self):
		return self.title 


class Powder(models.Model):

	title = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=7,decimal_places=3)
	description = models.TextField(null=True , blank=True)

	def __str__(self):
		return self.title 

class Roast(models.Model):

	title = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=7,decimal_places=3)
	description = models.TextField(null=True , blank=True)

	def __str__(self):
		return self.title 

class Syrup(models.Model):

	title = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=7,decimal_places=3)
	description = models.TextField(null=True , blank=True)

	def __str__(self):
		return self.title 

class Coffee(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=20)
	bean = models.ForeignKey(Bean, default=1)
	roast = models.ForeignKey(Roast, default=1)
	syrup = models.ManyToManyField(Syrup)
	powder = models.ManyToManyField(Powder)
	water = models.FloatField()
	milk = models.BooleanField(default=False) 
	shots = models.PositiveIntegerField(default=1)
	extra = models.TextField(null=True,blank=True) 
	price = models.DecimalField(max_digits=7,decimal_places=3, null=True)

	def __str__(self):
		return self.name 











