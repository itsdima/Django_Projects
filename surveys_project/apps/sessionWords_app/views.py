# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages 
from time import localtime, strftime

def index(request):
	if 'words' not in request.session:
		request.session['words'] = []
	return render(request, 'sessionWords_app/index.html')

def addword(request):
	if len(request.POST['newword']) < 1:
		messages.warning(request,'Field Cannot Be Empty!')
		return redirect('/session_words')
	if 'colors' not in request.POST:
		messages.warning(request, 'Field Cannot Be Empty!')
		return redirect('/session_words')
	font = '18px;'
	if 'bigfont' in request.POST:
		font = '25px;'
	newword = {
	 'word': request.POST['newword'],
	 'color': request.POST['colors'],
	 'time': strftime("%I: %M %p, %b %d, %y", localtime()),
	 'font': font
	 }
	request.session['words'].append(newword)
	request.session.modified = True

	return redirect('/session_words')

def clear(request):
	request.session.clear()
	return redirect('/session_words')




# Create your views here.
