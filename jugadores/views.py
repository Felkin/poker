# coding=utf-8

from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext

def index(request):
	return render_to_response('jugadores/index.html', context_instance=RequestContext(request))

def logueo(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			# Redirect to a success page.
			return render_to_response('jugadores/logged.html')
		else:
			return render_to_response('jugadores/index.html', {
				'error': 'Cuenta deshabilitada'
			}, context_instance=RequestContext(request))
			# Return a 'disabled account' error message
	else:
		# Return an 'invalid login' error message.
		return render_to_response('jugadores/index.html', {
			'error': 'Autentificación no válida'
		}, context_instance=RequestContext(request))

