from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


def placeholder(request):
	return HttpResponse("<h1> Avert your eyes for decency's sake.</h1>")


def usersignup(request): 
	context = {}
	form = UserSignup()
	context['form'] = form
	if request.method == "POST":
		form = UserSignup(request.POST)
		if form.is_valid():

			user = form.save(commit=False)
			username = user.username
			password = user.password
			user.set_password(password)
			user.save()
			auth_user = authenticate(username=username, password=password)
			login(request, auth_user)

			return redirect("ingredients:placeholder")
		# messages.error(request, forms.errors)
		# return redirect("posts:signup")
	return render(request,'signup.html', context)


def userlogin(request):
	context = {}
	form = UserLogin()
	context['form'] = form
	if request.method == "POST":
		form = UserLogin(request.POST)
		if form.is_valid():
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			
			if auth_user is not None:
				login(request,auth_user)
				return redirect("ingredients:placeholder")
			
			messages.warning(request, "Wrong username/password combination. Please try again.")
			return redirect("ingredients:login")
		messages.warning(request, form.errors)
		return redirect("ingredients:login")
		
	return render(request,'login.html', context)




def userlogout(request):
	logout(request)
	return redirect("ingredients:placeholder") 

def doing_gods_work_bean(request):
	if not (request.user.is_superuser or request.user.is_staff):
		raise Http404
	form = BeanInput(request.POST or None)
	if form.is_valid():
		
		form.save()
		messages.success(request, "Bean registered.")
		return redirect("ingredients:placeholder")

	objects = {
		"form":form,
	}
	return render(request, 'bean_create.html', objects)


def doing_gods_work_powder(request):
	if not (request.user.is_superuser or request.user.is_staff):
		raise Http404
	form = PowderInput(request.POST or None)
	if form.is_valid():
		
		form.save()
		messages.success(request, "Powder registered.")
		return redirect("ingredients:placeholder")

	objects = {
		"form":form,
	}
	return render(request, 'powder_create.html', objects)


def doing_gods_work_roast(request):
	if not (request.user.is_superuser or request.user.is_staff):
		raise Http404
	form = RoastInput(request.POST or None)
	if form.is_valid():
		
		form.save()
		messages.success(request, "Roast registered.")
		return redirect("ingredients:placeholder")

	objects = {
		"form":form,
	}
	return render(request, 'roast_create.html', objects)



def doing_gods_work_syrup(request):
	if not (request.user.is_superuser or request.user.is_staff):
		raise Http404
	form = SyrupInput(request.POST or None)
	if form.is_valid():
		
		form.save()
		messages.success(request, "Syrup registered.")
		return redirect("ingredients:placeholder")

	objects = {
		"form":form,
	}
	return render(request, 'syrup_create.html', objects)




def updating_gods_work_bean(request, bean_id):
	instance = get_object_or_404(Bean, id=bean_id)
	form = BeanInput(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect("ingredients:list")
	context = {
	"form":form,
	"instance": instance,
	"title": "Update",
	}
	return render(request, 'bean_update.html', context)

def updating_gods_work_powder(request, powder_id):
	instance = get_object_or_404(Powder, id=powder_id)
	form = PowderInput(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect("ingredients:list")
	context = {
	"form":form,
	"instance": instance,
	"title": "Update",
	}
	return render(request, 'powder_update.html', context)

def updating_gods_work_roast(request, roast_id):
	instance = get_object_or_404(Roast, id=roast_id)
	form = RoastInput(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect("ingredients:list")
	context = {
	"form":form,
	"instance": instance,
	"title": "Update",
	}
	return render(request, 'roast_update.html', context)

def updating_gods_work_syrup(request, syrup_id):
	instance = get_object_or_404(Syrup, id=syrup_id)
	form = SyrupInput(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect("ingredients:list")
	context = {
	"form":form,
	"instance": instance,
	"title": "Update",
	}
	return render(request, 'syrup_update.html', context)





def bean_delete(request, bean_id):
	instance = get_object_or_404(Bean, id=bean_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("ingredients:list")


def powder_delete(request, powder_id):
	instance = get_object_or_404(Powder, id=powder_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("ingredients:list")

def roast_delete(request, roast_id):
	instance = get_object_or_404(Roast, id=roast_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("ingredients:list")

def syrup_delete(request, syrup_id):
	instance = get_object_or_404(Syrup, id=syrup_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("ingredients:list")

def the_ol_mallet(request, coffee_id):
	instance = get_object_or_404(Coffee, id=coffee_id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("ingredients:list")

def create_coffee(request): 
	form = CoffeeInput(request.POST or None)
	if form.is_valid():
		obj = form.save()
		obj.user = request.user	
		obj.price = price(coffee= obj) 
		obj.save()
		messages.success(request, "Coffee registered.")
		return redirect("ingredients:placeholder")

	objects = {
		"form":form,
	}
	return render(request, 'coffee_create.html', objects)



def coffee_list(request):
	# today= timezone.now().date()
	
	obj_list = Coffee.objects.all()
	
	
	# paginator = Paginator(obj_list, 5) 

	# page = request.GET.get('page')
	# try:
	# 	p_objects = paginator.page(page) 
		
	# except PageNotAnInteger:
	# 	# If page is not an integer, deliver first page.
	# 	p_objects = paginator.page(1)
	# except EmptyPage:
	# 	# If page is out of range (e.g. 9999), deliver last page of results.
	# 	p_objects = paginator.page(paginator.num_pages)

	
	context = {
		"coffee_list": obj_list,
		# "today" : today,
	}
	return render(request, 'coffee_list.html', context)

def coffee_detail(request, coffee_id):
	obj = get_object_or_404(Coffee, id=coffee_id)

	context = {
	"obj" : obj

	}
		
	return render(request, 'detail.html', context)



def price(coffee):
	
	bean_price = coffee.bean.price
	roast_price = coffee.roast.price
	powder_price = 0
	syrup_price = 0
	
	for powder in coffee.powder.all():

		powder_price += powder.price 

	for syrup in coffee.syrup.all():
		
		syrup_price += syrup.price

	total_price = bean_price + roast_price + powder_price + syrup_price 
	return total_price

	




























