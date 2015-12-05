from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render_to_response
from django.template import RequestContext
import json
import urllib

########## GLOBAL VARIABLES ##########

########## PAGE MAPS ##########
def landing(request):
	return render(request, 'landing.html')

########## OTHER/ALGORITHMS/RECOMMENDATIONS ##########