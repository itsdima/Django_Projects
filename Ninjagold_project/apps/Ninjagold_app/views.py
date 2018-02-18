# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
import random 
from time import localtime, strftime

def index(request):
	if 'totalgold' not in request.session:
		request.session['totalgold'] = 0
	if 'log' not in request.session:
		request.session['log'] = []
	return render(request, 'Ninjagold_app/index.html')

def process(request):
	color = 'green'
	if request.POST['action'] == 'farm':
		num = random.randint(10, 20)
		request.session['totalgold'] += num
		message = 'You Earned ' + str(num) + ' golds from Farm!'
	if request.POST['action'] == 'cave':
		num = random.randint(5, 10)
		request.session['totalgold'] += num
		message = 'You Earned ' + str(num) + ' golds from Cave!'
	if request.POST['action'] == 'house':
		num = random.randint(2, 5)
		request.session['totalgold'] += num
		message = 'You Earned ' + str(num) + ' golds from House!'
	if request.POST['action'] == 'casino':
		num = random.randint(-50, 50)
		request.session['totalgold'] += num
		if num > 0:
			message = 'You entered casino and earned ' + str(num) + ' golds! NICE!'
		else:
			color = 'red'
			message = 'You entered casino and lost ' + str(num) + ' golds... OUCH!'
	printlog = {
		'color': color,
		'message': message,
		'time': strftime("%I: %M %p, %b %d, %y", localtime())
	}

	request.session['log'].append(printlog)
	request.session.modified = True
		
	return redirect('/')

def restart(request):
	request.session.clear()
	return redirect('/')

# Create your views here.
