from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from principal.forms import *
from principal.models import *
from google.appengine.api import users
from util.login_required import check_login


def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

@check_login
def lista_proyectos(request):
	proyectos = Proyecto.all()
	return render_to_response('proyectos.html', {'proyectos':proyectos},
		context_instance=RequestContext(request)
	)

@check_login
def new(request):
	if request.method == 'POST':
		formulario = newProyecto(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/proyectos')
	else:
		formulario = newProyecto()

	return render(request, 'proyectoform.html',
		{'formulario':formulario},
	)

def login(request):
	user = users.get_current_user()
	if not user:
		return HttpResponseRedirect(users.create_login_url("/privado"))
	else:
		return HttpResponseRedirect('/privado')

def logout(request):
	return HttpResponseRedirect(users.create_logout_url("/"))

@check_login
def privado(request):
	return render_to_response('privado.html', {'user':users},context_instance=RequestContext(request))





