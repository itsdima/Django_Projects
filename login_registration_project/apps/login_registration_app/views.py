# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages


# Create your views here.

def index(request):
	return render(request, 'login_registration_app/index.html')

def register(request):
	result = User.objects.registrationValidate(request.POST)
	print result
	if result['status']:
		request.session['user_id'] = result['user'].id
	else: 
		for error in result['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['reg_log'] = 'Registered'
	return redirect('/success')

def login(request):
	result = User.objects.loginValidate(request.POST)
	if result['status'] == False:
		for error in result['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['user_id'] = result['user'].id
	request.session['reg_log'] = 'Logged In'
	return redirect('/success')

def logout(request):
	request.session.clear()
	return redirect('/')

def success(request):
	if 'user_id' not in request.session:
		return redirect('/')
	if 'reg_log' not in request.session:
		return redirect('/')
	tempid= request.session['user_id']
	ActiveUser = User.objects.get(id=tempid)
	context = {
	'id': ActiveUser.id,
	'name': ActiveUser.first_name,
	'type': request.session['reg_log']
	}
	return render(request, 'login_registration_app/success.html', context)
