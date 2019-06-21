from django import forms

class Loginform(forms.Form):
	user = forms.CharField(max_langth = 100)
	password = forms.CharField(widget = forms.PasswordInput())
