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
            '''Tendría que llamar a otro metodo que pida el resto de datos del usuario y lo registre'''
            print ("Usuario registrado correctamente")
            archivo.write("\n" + datos_usuario)


    @staticmethod
    '''
    muestra las peliculas y crea los objetos pelicual y serie
    hay que crearlos, ya se estan sacando los datos uno por uno
    '''
    def cargarCatalogo():
        archivo = open("datos/catalogo.txt", "r")

        linea = archivo.readline()

        while linea != "":
            print linea
            pos1 = 0
            pos2 = linea.find(",")
            while pos2 != -1:
                tipo = linea[pos1: pos2].lstrip(" ")
                print tipo
                pos1 = pos2
                pos2 = linea.find(",", pos1+1)
                print pos2

            linea = archivo.readline()

