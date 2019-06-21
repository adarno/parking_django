from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns =  [  path('', views.index, name='index'), 
		  path('familie_click', views.familie_click, name='familie_click'),
	 	  path('normal_click', views.normal_click, name='normal_click'),
		  path('frauenparkplatz_click', views.frauenparkplatz_click, name='frauenparkplatz_click'),
		  ]
