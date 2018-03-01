# -*- coding: utf-8 -*-

from Util import Util
from modelo.Usuario import Usuario

'''
	Aplicación de streaming de series. Toda la gestión y documentación en...
	-> https://github.com/ismenc/python-gestor-series
	@author: Diego, Ismael, Davinia, Eduardo & Ricardo
'''


''' PROBLEMAS PARA EJECUTAR? -> https://github.com/ismenc/python-gestor-series#7-problemas-y-soluciones '''


''' -------------- Programa principal -------------- '''

on = True
while on:
	#Llamada a la funcion para solicitar los datos
	user = Util.solicitarCadena("Introduce el nombre de usuario: ")
	password = Util.solicitarCadena("Introduce la contraseña: ")
	
	# Hacemos el login de usuario y cargamos los elementos necesarios
	usuario = Util.logear(user, password)
	pelis = Util.cargarCatalogoPeliculas()
	series = Util.cargarCatalogoSeries()
	
	sesion_activa = True
	while sesion_activa == True:
		# Mostramos el menú con las opciones https://github.com/ismenc/python-gestor-series/blob/master/doc/enunciado-practica.pdf
		sesion_activa = Util.tratar_menu(usuario, pelis, series)
	
	salir = Util.preguntarSiNo("Desea salir de la aplicación? (si/no)")
	if(salir == "si"):
		on = False
		print("shutting down...")