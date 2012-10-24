"""Decorators for the authentication framework."""

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from google.appengine.api import users

def check_login(fn):	
	def wrapper(request, *args, **krargs):
		user = users.get_current_user()
		if not user:
			return HttpResponseRedirect(users.create_login_url(request.path))
		else:
			return fn(request, *args, **krargs)
	return wrapper