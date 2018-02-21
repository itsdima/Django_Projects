# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def index(request):
	return render(request, 'surveys_app/index.html')

def result(request):
	print request.session['context']
	return render(request, 'surveys_app/result.html')
def process(request):
	if len(request.POST['name']) < 1:
		messages.error(request,'Name Cannot Be Empty!')
		return redirect('/')
	if len(request.POST['comment']) > 120:
		messages.error(request,'Comment should be less than 120 characters!')
		return redirect('/')
	if 'times' in request.session:
		request.session['times'] += 1
	else:
		request.session['times']=1
	context = {
	'name': request.POST['name'],
	'location': request.POST['location'], 
	'language': request.POST['language'],
	'comment': request.POST['comment']
	}
	request.session['context'] = context

	return redirect('/result')

# Create your views here.
