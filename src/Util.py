# -*- coding: utf-8 -*-

'''
    Clase auxiliar que provee a nuestra aplicación de las funciones necesarias.
    
Created on 16 feb. 2018
@author: Diego
'''
class Util():

    @staticmethod
    def logear(datos_usuario):
        ''' Nos permite logearnos si el usuario está en la base de datos o lo registra si no está. '''
        archivo = open("datos/usuarios.txt", "r+")

        linea = archivo.readline()
        usuario_encontrado = False

        while linea != "" and usuario_encontrado == False:
            if linea.find(datos_usuario) == 0:
                print ("Logueado correctamente")
                usuario_encontrado = True
            else:
                linea = archivo.readline()

        if usuario_encontrado == False:
            print ("Usuario registrado correctamente")
            archivo.write("\n" + datos_usuario)

    '''
    @staticmethod
    def cargarCatalogo(rutaCatalogo):
        archivo = open(rutaCatalogo, "r")
        for linea in archivo.readLines():
    
    '''