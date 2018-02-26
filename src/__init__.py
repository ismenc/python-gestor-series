# -*- coding: utf-8 -*-
import os
from Util import Util

'''
	Aplicación de streaming de series. Toda la gestión y documentación en...
	-> https://github.com/ismenc/python-gestor-series
'''

'''
	funcion que muestra el menú de la aplicación
	sacado de esta página
	--> https://www.lawebdelprogramador.com/codigo/Python/2935-Ejemplo-de-implementar-un-menu-en-python-en-la-consola.html
'''
def mostrar_menu():
	#os.system('clear')#limpia la pantalla antes de mostrar el menú (hay que hacer import os)
	print ("Selecciona una opción")
	print ("\t1 - Ver catálogo")
	print ("\t2 - Ver una serie")
	print ("\t3 - Ver una pelicula")
	print ("\t4 - Ver peliculas vistas")
	print ("\t5 - Ver peliculas pendientes")
	print ("\t6 - Ver series vistas")
	print ("\t7 - Ver series pendientes")
	print ("\t9 - Cerrar sesion")
	

def tratar_menu():
	sesion_cerrada = False
	opcion = 0
	
	while sesion_cerrada != True:
		mostrar_menu()
		
		opcion = input("Introduce el número de la opcion elegida: ")
		
		if opcion == 1:
			print ("PROXIMAMENTE. Ver catálogo.")
			Util.cargarCatalogo()
			
		elif opcion == 2:
			print ("PROXIMAMENTE. Ver una serie.")
		
		elif opcion == 3:
			print ("PROXIMAMENTE. Ver una pelicula.")
			
		elif opcion == 4:
			print ("PROXIMAMENTE. Ver una serie.")
		
		elif opcion == 5:
			print ("PROXIMAMENTE. Ver una pelicula.")
			
		elif opcion == 6:
			print ("PROXIMAMENTE. Ver una serie.")
		
		elif opcion == 7:
			print ("PROXIMAMENTE. Ver una pelicula.")
			
		elif opcion == 9:
			print ("Hasta pronto :D")
			sesion_cerrada = True
		
		else:
			print ("\n\tERROR. Elige una opcion correcta.")
			opcion = 0
	
	return sesion_cerrada


'''
	Funcion para solicitar los datos del usuario (podría integrarse en
	la clase Util)
'''
def solicitar_datos_inicio():
	nombre_usuario = raw_input("Introduce tu nombre de usuario: ")
	password = raw_input("Introduce tu contraseña: ")
	datos_usuario = nombre_usuario + ", " + password
		
	return datos_usuario


''' ----LLAMADA A LAS FUNCIONES---- '''
sesion = False
while sesion == False:
	#Llamada a la funcion para solicitar los datos
	datos_inicio = solicitar_datos_inicio()
	# Hacemos el login de usuario (en mi casa no va raw input)//Diego: pos en la clase no funciona sin raw_input xD
	Util.logear(datos_inicio)
	# Mostramos el menú con las opciones https://github.com/ismenc/python-gestor-series/blob/master/doc/enunciado-practica.pdf
	sesion = tratar_menu()








