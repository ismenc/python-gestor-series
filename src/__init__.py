# -*- coding: utf-8 -*-

from Util import Util

'''
	Aplicación de streaming de series. Toda la gestión y documentación en...
	-> https://github.com/ismenc/python-gestor-series
'''

# Hacemos el login de usuario (en mi casa no va raw input)

nombre_usuario = input("Introduce tu nombre de usuario: ")
password = input("Introduce tu contraseña: ")
datos_usuario = nombre_usuario + ", " + password

Util.logear(datos_usuario)

# Mostramos el menú con las opciones https://github.com/ismenc/python-gestor-series/blob/master/doc/enunciado-practica.pdf
