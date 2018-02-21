# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
	def registrationValidate(self, postData):
		response = {
			'status': True,
		}
		errors = []

		if not EMAIL_REGEX.match(postData['email']):
			errors.append('Invalid Email')
		if len(postData['first_name']) < 1 or len(postData['last_name']) < 1 or len(postData['email']) < 1 or len(postData['password']) < 1 or len(postData['confirm']) < 1:
			errors.append('Please fill all required fields!')
		if postData['password'] != postData['confirm']:
			errors.append('Passwords did not match!')
		if len(postData['password']) < 8:
			errors.append('Weak password, try 8 or more characters!')
		for letter in postData['first_name']:
			if letter.isdigit():
				errors.append('Your name cannot contain any numbers!')
		for letters in postData['last_name']:
			if letters.isdigit():
				errors.append('Your name cannot contain any numbers!')
		if len(errors) > 0:
			response['status'] = False
			response['errors'] = errors
		else: 
			PW = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			response['user'] = User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=PW)
		return response

	def loginValidate(self, postData):
		response = {
			'status': False,
		}
		errors = []
		users = User.objects.filter(email=postData['logemail'])
		if len(users) < 1:
			errors.append('Incorrect Email/Password, Try again')
			response['errors'] = errors
			return response
		PW = bcrypt.checkpw(postData['logpassword'].encode(), users[0].password.encode())
		if PW == True:
			response['status'] = True
			response['user'] = users[0]
		else: 
			errors.append('Incorrect Email/Password, Try again')
			response['errors'] = errors
		return response




class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	objects = UserManager()

	def __str__(self):
		return self.first_name
