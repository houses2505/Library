# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class LibroForm(forms.ModelForm):
	class Meta:
		model = Libro
		fields = '__all__'
		widgets = {
			'nombre_libro': TextInput(attrs = {'class': 'form-control', 'maxlength': '100', 'required': True}),
		}
		labels = {
			'nombre_libro': 'Nombre libro',
		}