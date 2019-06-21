from django.shortcuts import render
from django.http import HttpResponse
#from mysite_parkinglot.forms import LoginForm
#from django.template import loader

test = 0
your_spot = 1

def index(request):
	
	return render_page(request)


def familie_click(request):
	print("Familienparkplatz")
	return render_page(request)

def normal_click(request):
	print("normaler parkplatz")
	return render_page(request)

def frauenparkplatz_click(request):
	print("Faruenparkplatz")
	return render_page(request)

def render_page(request):
	return render(request, 'polls/index.html', {"number_spots" : test, "your_spot" : your_spot})


# Create your views here.
