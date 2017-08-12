from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import *
from .models import *
from .forms import *

class LibroCrearView(CreateView):
	template_name = 'layout/form_general.html'
	success_message = 'Libro agregado con exito'
	success_url = '/libros'
	form_class = LibroForm

	def get_context_data(self, **kwargs):
		context = super(LibroCrearView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar Multimedia'
		context['url'] = reverse('crear_libro')
		return context

class LibroListarView(ListView):
	template_name = 'library/lista.html'
	model = Libro

class LibroEditarView(UpdateView):
	template_name = 'layout/form_general.html'
	success_message = 'Libro actualizado con exito'
	success_url = '/libros/lista'
	model = Libro
	form_class = LibroForm

	def get_context_data(self, **kwargs):
		context = super(LibroEditarView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar Multimedia'
		context['url'] = reverse('editar_libro', kwargs = {'pk': self.kwargs['pk']})
		return context

class LibroEliminarView(DeleteView):
	model = Libro
	template_name = 'library/delete.html'
	success_url = '/libros/lista'