from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, "mcoder/home.html")


def contact(request):
	return HttpResponse("home/Contact")


def about(request):
	return HttpResponse("home/About")
