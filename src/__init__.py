# -*- coding: utf-8 -*-
import os
from Util import Util

'''
	Aplicación de streaming de series. Toda la gestión y documentación en...
	-> https://github.com/ismenc/python-gestor-series
	@author: Diego, Ismael, Davinia, Eduardo & Ricardo
'''


''' -------------- Programa principal -------------- '''

#Llamada a la funcion para solicitar los datos
print("Introduce el nombre de usuario: ")
user = raw_input()
print("Introduce la contraseña: ")
user = raw_input()

# Hacemos el login de usuario y cargamos los elementos necesarios
usuario = Util.logear(user, password)
pelis = Util.cargarCatalogoPeliculas()
series = Util.cargarCatalogoSeries()

sesion_activa = True
while sesion_activa == True:
	# Mostramos el menú con las opciones https://github.com/ismenc/python-gestor-series/blob/master/doc/enunciado-practica.pdf
	sesion_activa = Util.tratar_menu(usuario, pelis, series)

