# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import localtime, strftime

def index(request):
	context = {
	"date": strftime("%b %d, %y", localtime()),
	"time": strftime("%I: %M %p", localtime())
	}
	return render(request, 'index.html', context)

# Create your views here.
