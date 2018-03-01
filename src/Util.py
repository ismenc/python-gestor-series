# -*- coding: utf-8 -*-

import modelo.Usuario as U
import modelo.Pelicula as P
import modelo.Serie as S
#from pip._vendor.distlib.compat import raw_input
#from builtins import int
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
            print ("Procedemos a registrar un nuevo usuario.\nUsuario registrado correctamente.")
            archivo.write("\n" + user + ", " + password)
            usuario = U.Usuario(user, password, 22)
        return usuario
    
    

    ''' Devuelve un número entero leído y validado '''
    @staticmethod
    def leerEntero():
        
        try:
            numero = input()
            valor = int(numero)
        except NameError, ValueError:
            print ("Debes introducir un número. Intenta de nuevo, tu puedes!")
            valor = Util.leerEntero()
            
        return valor
    

    ''' Carga el catálogo de películas en una lista '''
    @staticmethod
    def cargarCatalogoPeliculas():
        archivo = open("datos/catalogo-peliculas.txt", "r")
        
        peliculas = []
        linea = archivo.readline()

        while linea != "":
            datos = linea.split(',')
            titulo = datos[0]
            fechaEstreno = datos[1]
            genero = datos[2]
            director = datos[3]
            duracion = datos[4]
            
            peliculas.append(P.Pelicula(titulo, fechaEstreno, genero, director, duracion))
            
            linea = archivo.readline()
        return peliculas
    
    
    ''' 
        Carga el catálogo de series en una lista 
    '''
    @staticmethod
    def cargarCatalogoSeries():
        archivo = open("datos/catalogo-series.txt", "r")
        
        print ("Catálogo de películas:")
        series = []
        linea = archivo.readline()

        while linea != "":
            datos = linea.split(',')
            titulo = datos[0]
            fechaEstreno = datos[1]
            genero = datos[2]
            director = datos[3]
            
            # El array de temporadas me parecería más fácil si fuese la siguiente línea
            linea = archivo.readline()
            temporadas = linea.split(',')
            
            series.append(S.Serie(titulo, fechaEstreno, genero, director, temporadas))
            
            linea = archivo.readline()
        return series
    
    
    ''' Muestra por pantalla el mensaje y a continuación la lista de películas o series que le pasemos '''
    @staticmethod
    def mostrarLista(msg, lista):
        print (msg + "\n" + "\n".join(str(lista.index(p)+1) +" - "+ p.toString() for p in lista))


    '''
        Funcion que muestra el menú de la aplicación
        sacado de esta página
        --> https://www.lawebdelprogramador.com/codigo/Python/2935-Ejemplo-de-implementar-un-menu-en-python-en-la-consola.html
    '''
    @staticmethod
    def mostrar_menu():
        #os.system('clear')#limpia la pantalla antes de mostrar el menú (hay que hacer import os)
        print ("--------------------- Menú ---------------------")
        print ("\t1 - Ver catálogo de películas")
        print ("\t2 - Ver catálogo de series")
        print ("\t3 - Ver una serie")
        print ("\t4 - Añadir una serie a pendientes")
        print ("\t5 - Ver una pelicula")
        print ("\t6 - Añadir una película a pendientes")
        print ("\t7 - Mostrar películas y series vistas")
        print ("\t8 - Mostrar películas y series pendientes")
        print ("\t9 - Cerrar sesion")
        print ("------------------------------------------------")
        
    
    '''
        Función que resuelve toda la casuística correspondiente a la opción elegida por el usuario.
        Devuelve si la sesión sigue activa para que el main pueda finalizar.
    '''
    @staticmethod
    def tratar_menu(usuario, peliculas, series):
        sesion_activa = True
        opcion = 0
        
        while sesion_activa != False:
            Util.mostrar_menu()
        
            print("Introduce el número de la opcion elegida: ")
            opcion = Util.leerEntero()
            
            if opcion == 1:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                
            elif opcion == 2:
                Util.mostrarLista("Las series disponibles son: ", series)
                
            elif opcion == 3:
                Util.mostrarLista("Las series disponibles son: ", series)
                print ("Introduzca el número de serie para ver: ")
                numero = Util.leerEntero()
                try:
                    usuario.addAVisto(series[numero-1].titulo)
                except IndexError:
                    print("Error. Debe seleccionar una serie de la lista.")
            
            elif opcion == 4:
                Util.mostrarLista("Las series disponibles son: ", series)
                print ("Introduzca el número de serie para añadir a pendientes: ")
                numero = Util.leerEntero()
                try:
                    usuario.addAPendienteVer(series[numero-1].titulo)
                except IndexError:
                    print("Error. Debe seleccionar una serie de la lista.")
                
            elif opcion == 5:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                print ("Introduzca el número de película para ver: ")
                numero = Util.leerEntero()
                try:
                    usuario.addAVisto(peliculas[numero-1].titulo)
                except IndexError:
                    print("Error. Debe seleccionar una película de la lista.")
            
            elif opcion == 6:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                print ("Introduzca el número de película para añadir a pendientes: ")
                numero = Util.leerEntero()
                try:
                    usuario.addAPendienteVer(peliculas[numero-1].titulo)
                except IndexError:
                    print("Error. Debe seleccionar una película de la lista.")
            
            elif opcion == 7:
                usuario.verVisto()
        
            elif opcion == 8:
                usuario.verPendientes()
                
            elif opcion == 9:
                print ("Hasta pronto :D")
                sesion_activa = False
            
            else:
                print ("\n\tError. Debes elegir una opción correcta.")
                opcion = 0
        
        return sesion_activa
    
    
    
    