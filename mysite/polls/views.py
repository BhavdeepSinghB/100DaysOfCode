from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello World")

def detail(request, questionid):
	return HttpResponse("You're looking at question {}".format(questionid))

def results(request, questionid):
	response = "You're looking at results for question {}".format(questionid)
	return HttpResponse(response)

def vote(request, questionid):
	return HttpResponse("You're voting for question {}".format(questionid))