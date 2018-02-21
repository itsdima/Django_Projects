# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse 
from django.contrib import messages
from .models import *
# Create your views here.

def index(request):
	allcourses = {
	'thiscourse': Course.objects.all()
	}
	return render(request, 'courses_app/index.html', allcourses)

def destroy(request, number):
	Delete = Course.objects.get(id=number)
	context = {
	'name': Delete.name,
	'desc': Delete.desc,
	'id': Delete.id
	}
	return render(request, 'courses_app/destroy.html', context)

def process(request, number):
	Destroy = Course.objects.get(id=number)
	Destroy.delete()
	return redirect('/')

def add(request):
	if len(request.POST['name']) < 1 or len(request.POST['desc']) < 1:
		messages.error(request, 'Fill out all required fields!')
		return redirect('/')
	NewCourse = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
	return redirect('/')
