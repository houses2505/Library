from django.conf.urls import patterns, url, include
from .views import *

urlpatterns = patterns('libro.views',
	url(r'^$', LibroCrearView.as_view(), name = 'crear_libro'),
	url(r'^lista/$', LibroListarView.as_view(), name = 'listar_libro'),
	url(r'^editar/(?P<pk>\d+)/$', LibroEditarView.as_view(), name = 'editar_libro'),
	url(r'^eliminar/(?P<pk>\d+)/$', LibroEliminarView.as_view(), name = 'eliminar_libro'),
)
