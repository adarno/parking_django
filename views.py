from django.shortcuts import render
from django.http import HttpResponse
#from mysite_parkinglot.forms import LoginForm
#from django.template import loader

def index(request):
	
	return render(request, 'polls/index.html')


def familie_click(request):
	print("Familienparkplatz")
	return render(request, 'polls/index.html')

def normal_click(request):
	print("normaler parkplatz")
	return render(request, 'polls/index.html')

def frauenparkplatz_click(request):
	print("Faruenparkplatz")
	return render(request, 'polls/index.html')


# Create your views here.
