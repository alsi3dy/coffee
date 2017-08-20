from django import forms
from django.contrib.auth.models import User
from .models import *

class UserSignup(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']

		widgets={
		'password': forms.PasswordInput()
		}
		
class UserLogin(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

class BeanInput(forms.ModelForm):
	price = forms.DecimalField(required=True, max_digits=7, min_value=0)
	class Meta: 
		model = Bean
		fields = ['title','price','description']

class PowderInput(forms.ModelForm):
	class Meta: 
		model = Powder
		fields = ['title','price','description']  

class RoastInput(forms.ModelForm):
	class Meta: 
		model = Roast
		fields = ['title','price','description']

class SyrupInput(forms.ModelForm):
	class Meta: 
		model = Syrup
		fields = ['title','price','description']

class CoffeeInput(forms.ModelForm):
	class Meta:
		model = Coffee 
		fields = ['name','bean','powder','roast','syrup' ,'water','milk','shots','extra']









