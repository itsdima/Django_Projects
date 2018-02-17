# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
	random_word = get_random_string(length=14)
	context = {
	'word': random_word
	}
	if 'count' in request.session: 
		request.session['count'] += 1
	else: 
		request.session['count'] = 1
	return render(request, 'index.html', context)

def reset(request):
	request.session['count'] = 0
	return redirect('/')

# Create your views here.
