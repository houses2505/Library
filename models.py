from __future__ import unicode_literals

from django.db import models

class Libro(models.Model):
	nombre_libro = models.CharField(max_length = 100)
	referencia_libro = models.CharField(max_length = 15)

	def __str__(self):
		return self.nombre_libro