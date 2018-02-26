# -*- coding: utf-8 -*-

import modelo.Usuario as U
import modelo.Pelicula as P
import modelo.Serie as S
from pip._vendor.distlib.compat import raw_input
from builtins import int
from modelo.Pelicula import Pelicula

'''
    Clase auxiliar que provee a nuestra aplicación de las funciones necesarias.

Created on 16 feb. 2018
@author: Diego
'''
class Util():

    ''' Nos permite logearnos si el usuario está en la base de datos o lo registra si no está. '''
    @staticmethod
    def logear(user, password):
        archivo = open("datos/usuarios.txt", "r+")

        linea = archivo.readline()
        usuario_encontrado = False

        while linea != "" and usuario_encontrado == False:
            if linea.find(user + ", " + password) == 0:
                print ("Logueado correctamente")
                usuario_encontrado = True
                usuario = U.Usuario(user, password, 22)
            else:
                linea = archivo.readline()

        if usuario_encontrado == False:
            '''Tendría que llamar a otro metodo que pida el resto de datos del usuario y lo registre'''
            print ("Usuario registrado correctamente")
            archivo.write("\n" + user + ", " + password)
            usuario = U.Usuario(user, password, 22)
        return usuario
    

    ''' OBSOLETO
        Funcion para solicitar los datos del usuario (podría integrarse en la clase Util)
    '''
    @staticmethod
    def solicitar_datos_inicio():
        nombre_usuario = input("Introduce tu nombre de usuario: ")
        password = input("Introduce tu contraseña: ")
        datos_usuario = nombre_usuario + ", " + password
            
        return datos_usuario
    

    ''' Devuelve un número entero leído y validado '''
    @staticmethod
    def leerEntero():
        numero = raw_input()
        try:
            valor = int(numero)
        except ValueError:
            print ("Debes introducir un número. Intenta de nuevo, tu puedes!")
            valor = Util.leerEntero()
        return valor
    

    ''' Carga el catálogo de películas en una lista '''
    @staticmethod
    def cargarCatalogoPeliculas():
        archivo = open("datos/catalogo-peliculas.txt", "r")
        
        print ("Catálogo de películas:")
        linea = archivo.readline()

        i = 0
        while linea != "":
            pos1 = 0
            pos2 = linea.find(",")
            titulo = linea[pos1: pos2]
            pos1 = pos2
            pos2 = linea.find(",")
            fechaEstreno = linea[pos1: pos2]
            pos1 = pos2
            pos2 = linea.find(",")
            genero = linea[pos1: pos2]
            pos1 = pos2
            pos2 = linea.find(",")
            director = linea[pos1: pos2]
            pos1 = pos2
            duracion = linea[pos1: len(linea)-1]
            
            peliculas = []
            peliculas[i] = P.Pelicula(titulo, fechaEstreno, genero, director, duracion)
            i = i + 1
            
            linea = archivo.readline()
        return peliculas
    
    
    ''' WORK IN PROGRESS
        Carga el catálogo de series en una lista 
    '''
    @staticmethod
    def cargarCatalogoSeries():
        archivo = open("datos/catalogo-peliculas.txt", "r")
        
        print ("Catálogo de películas:")
        linea = archivo.readline()

        i = 0
        while linea != "":
            pos1 = 0
            pos2 = linea.find(",")
            titulo = linea[pos1: pos2]
            pos1 = pos2
            pos2 = linea.find(",")
            fechaEstreno = linea[pos1: pos2]
            pos1 = pos2
            pos2 = linea.find(",")
            genero = linea[pos1: pos2]
            pos1 = pos2
            pos2 = linea.find(",")
            director = linea[pos1: pos2]
            pos1 = pos2
            duracion = linea[pos1: len(linea)-1]
            
            # El array de temporadas me parecería más fácil si fuese la siguiente línea
            linea = archivo.readline()
            ''' temporadas = linea (?) '''
            
            series = []
            series[i] = S.Serie(titulo, fechaEstreno, genero, director, duracion, [1, 2, 3])
            i = i + 1
            
            linea = archivo.readline()
        return series
    
    
    ''' Muestra por pantalla el mensaje y a continuación la lista de películas o series que le pasemos '''
    @staticmethod
    def mostrarLista(msg, lista):
        print (msg + "\n".join(lista))
        

    '''
        Funcion que muestra el menú de la aplicación
        sacado de esta página
        --> https://www.lawebdelprogramador.com/codigo/Python/2935-Ejemplo-de-implementar-un-menu-en-python-en-la-consola.html
    '''
    @staticmethod
    def mostrar_menu():
        #os.system('clear')#limpia la pantalla antes de mostrar el menú (hay que hacer import os)
        print ("Selecciona una opción")
        print ("\t1 - Ver catálogo de películas")
        print ("\t2 - Ver catálogo de series")
        print ("\t3 - Ver una serie")
        print ("\t4 - Añadir una serie a pendientes")
        print ("\t5 - Ver una pelicula")
        print ("\t6 - Añadir una película a pendientes")
        print ("\t7 - Mostrar películas y series vistas")
        print ("\t8 - Mostrar peíiculas y series pendientes")
        print ("\t9 - Cerrar sesion")
        
    
    '''
        Función que resuelve toda la casuística correspondiente a la opción elegida por el usuario.
    '''
    @staticmethod
    def tratar_menu(usuario, peliculas, series):
        sesion_activa = True
        opcion = 0
        
        while sesion_activa != False:
            Util.mostrar_menu()
        
            opcion = input("Introduce el número de la opcion elegida: ")
            
            if opcion == 1:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                
            elif opcion == 2:
                Util.mostrarLista("Las series disponibles son: ", series)
                
            elif opcion == 3:
                Util.mostrarLista("Las series disponibles son: ", series)
                print ("Selecciona una serie para ver: ")
                numero = Util.leerEntero()
                usuario.addAVisto(series[numero])
            
            elif opcion == 4:
                Util.mostrarLista("Las series disponibles son: ", series)
                print ("Selecciona una serie para añadir a pendientes: ")
                numero = Util.leerEntero()
                usuario.addAPendienteVer(series[numero])
                
            elif opcion == 4:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                print ("Selecciona una Película para ver: ")
                numero = Util.leerEntero()
                usuario.addAVisto(peliculas[numero])
            
            elif opcion == 5:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                print ("Selecciona una Película para añadir a pendientes: ")
                numero = Util.leerEntero()
                usuario.addAPendienteVer(peliculas[numero])
            
            elif opcion == 6:
                usuario.verVisto()
        
            elif opcion == 7:
                usuario.verPendientes()
                
            elif opcion == 9:
                print ("Hasta pronto :D")
                sesion_activa = False
            
            else:
                print ("\n\tError. Debes elegir una opción correcta.")
                opcion = 0
        
        return sesion_activa