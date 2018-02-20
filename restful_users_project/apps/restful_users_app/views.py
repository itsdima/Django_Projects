# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import User

# Create your views here.

def index(request):
	allusers = {
	'thisuser': User.objects.all()
	}
	print allusers
	return render(request, 'restful_users_app/index.html', allusers)

def create(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	create = User.objects.create(first_name=first_name, last_name=last_name, email=email)
	userId = User.objects.last()
	print create
	return redirect('/users/'+ str(userId.id))

def new(request):
	return render(request, 'restful_users_app/new.html')

def edit(request, number):
	userID = User.objects.get(id=number)
	context = {
	'first_name': userID.first_name,
	'last_name': userID.last_name,
	'email': userID.email,
	'created': userID.created_at,
	'id': userID.id
	}
	return render(request, 'restful_users_app/edit.html', context)

def processchanges(request, number):
	editUser = User.objects.get(id=number)
	editUser.first_name = request.POST['first_name']
	editUser.last_name = request.POST['last_name']
	editUser.email = request.POST['email']
	editUser.save()
	return redirect('/')

def displayuser(request, number):
	userID = User.objects.get(id=number)
	context = {
	'first_name': userID.first_name,
	'last_name': userID.last_name,
	'email': userID.email,
	'created': userID.created_at,
	'id': userID.id
	}
	return render(request, 'restful_users_app/show.html', context)

def destroy(request, number):
	UserID = User.objects.get(id=number)
	UserID.delete()
	return redirect('/')

def update(request):
	return redirect('/')
