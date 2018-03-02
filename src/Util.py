# -*- coding: utf-8 -*-

import modelo.Usuario as U
import modelo.Pelicula as P
import modelo.Serie as S
import csv

'''
    Clase auxiliar que provee a nuestra aplicación de las funciones necesarias.

Created on 16 feb. 2018
@author: Diego
'''
class Util():
    
    ''' Solicitar cadena nombre o password '''
    @staticmethod
    def solicitarCadena(msg):
        print(msg)
        cadena = raw_input()
        
        if(len(str(cadena)) < 2):
            cadena = Util.solicitarCadena("Entrada no válida. "+msg)
        
        return cadena
    
    
    ''' Devuelve un número entero leído y validado '''
    @staticmethod
    def leerEntero(msg):
        
        print(msg)
        
        try:
            numero = raw_input()
            valor = int(numero)
        except NameError:
            print ("Debes introducir un número entero positivo. Intenta de nuevo, tu puedes!")
            valor = Util.leerEntero(msg)
        except ValueError:
            print ("Debes introducir un número entero positivo. Intenta de nuevo, tu puedes!")
            valor = Util.leerEntero(msg)
        if(valor < 1):
            print ("Debes introducir un número entero positivo. Intenta de nuevo, tu puedes!")
            valor = Util.leerEntero(msg)
            
        return valor
    
        
    ''' Preguntar si/no '''
    @staticmethod
    def preguntarSiNo(msg):
        respuesta = Util.solicitarCadena(msg)
        while respuesta != "si" and respuesta != "no":
            print("Error. Debe responder si/no.")
            respuesta = Util.preguntarSiNo(msg)
        
        return respuesta
    
    
    ''' Da de alta un nuevo usuario '''
    @staticmethod
    def registrarUsuario(user, password, edad):
        ''' Registra a un usuario en la base de datos '''
        
        usuario = U.Usuario(user, password, edad, None, None)
        archivo = open("datos/usuarios.txt", "a")
        
        print ("Procedemos a registrar un nuevo usuario.\nUsuario registrado correctamente.")
        archivo.write("\n" + user + "," + password +","+ str(edad))
        archivo.write(" ")
        archivo.write(" ")
        archivo.close()
        
        return usuario
    
    
    

    ''' Nos permite logearnos si el usuario está en la base de datos o lo registra si no está. '''
    @staticmethod
    def logear(user, password, usuarios):
        archivo = open("datos/usuarios.txt", "r+")

        linea = archivo.readline()
        usuario_encontrado = False

        try:
            # Buscamos al usuario en la base de datos.
            while linea != "" and usuario_encontrado == False:
                
                if linea.find(user + "," + password) == 0:
                    print ("Logueado correctamente")
                    usuario_encontrado = True
                    datos = linea.split(',')
                    # Este bloque comprueba si el usuario está en la lista de sesiones recientes
                    if(user not in usuarios):
                        vistos = archivo.readline().split(',')
                        if(len(vistos) < 2):
                            vistos = None
                        pendientes = archivo.readline().split(',')
                        if(len(pendientes) < 2):
                            pendientes = None
                        usuario = U.Usuario(datos[0], datos[1], int(datos[2]), vistos, pendientes)
                        usuarios[user] = usuario
                    else:
                        usuario = usuarios[user]
                else:
                    linea = archivo.readline()
    
    
            if usuario_encontrado == False:
                respuesta = Util.preguntarSiNo("Usuario no registrado. ¿Desea registrar el nuevo usuario? (si/no)")
                    
                if(respuesta == "si"):
                    edad = Util.leerEntero("Introduzca su edad:")
                    usuario = Util.registrarUsuario(user, password, edad)
                else:
                    user = Util.solicitarCadena("Introduce el nombre de usuario registrado: ")
                    password = Util.solicitarCadena("Introduce la contraseña: ")
                    usuario = Util.logear(user, password, usuarios)
        # Comprobación de errores
        except ValueError as error:
            print("Error registrando a usuario: " + str(error))
            user = Util.solicitarCadena("Login:\nIntroduce el nombre de usuario registrado: ")
            password = Util.solicitarCadena("Introduce la contraseña: ")
            usuario = Util.logear(user, password, usuarios)
            
        return usuario
    
    
    

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
            duracion = temporadas[0]
            temporadas.remove(temporadas[0])
            
            series.append(S.Serie(titulo, fechaEstreno, genero, director, duracion, temporadas))
            
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
            opcion = Util.leerEntero("Introduce el número de la opcion elegida: ")
            
            
            if opcion == 1:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                
                
                
            elif opcion == 2:
                Util.mostrarLista("Las series disponibles son: ", series)
                
                
                
            elif opcion == 3:
                Util.mostrarLista("Las series disponibles son: ", series)
                numero = Util.leerEntero("Introduzca el número de serie para ver: ")
                try:
                    usuario.addAVisto(series[numero-1].titulo)
                except IndexError:
                    print("Error. Debe seleccionar una serie de la lista.")
                    
                    
            
            elif opcion == 4:
                Util.mostrarLista("Las series disponibles son: ", series)
                numero = Util.leerEntero("Introduzca el número de serie para añadir a pendientes: ")
                try:
                    usuario.addAPendienteVer(series[numero-1].titulo)
                except IndexError:
                    print("Error. Debe seleccionar una serie de la lista.")
                    
                    
                
            elif opcion == 5:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                numero = Util.leerEntero("Introduzca el número de película para ver: ")
                try:
                    usuario.addAVisto(peliculas[numero-1].titulo)
                except IndexError:
                    print("Error. Debe seleccionar una película de la lista.")
                    
                    
            
            elif opcion == 6:
                Util.mostrarLista("Las películas disponibles son: ", peliculas)
                numero = Util.leerEntero("Introduzca el número de película para añadir a pendientes: ")
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
                
                archivo = open("datos/usuarios.txt", "r")
                linea = archivo.readline()
                usuario_encontrado = False
                while linea != "" and usuario_encontrado == False:
                    if linea.find(usuario.nombre + "," + usuario.clave + "," + str(usuario.edad)) == 0:
                        usuario_encontrado = True
                        indice = archivo.tell()
                    else:
                        linea = archivo.readline()
                archivo.close()
                
                '''archivo = open("datos/usuarios.txt", "w+")
                archivo.seek(indice)
                writer = csv.writer(archivo, delimiter=',')
                writer.writerows([usuario.visto, usuario.pendienteVer])
                archivo.close()'''
                
                bottle_list = []

                # Read all data from the csv file.
                with open('datos/usuarios.txt', 'rb') as b:
                    bottles = csv.reader(b)
                    bottle_list.extend(bottles)
                
                line_to_override = {numero:usuario.visto, numero+1:usuario.pendienteVer}
                
                # Write data to the csv file and replace the lines in the line_to_override dict.
                with open('datos/usuarios.txt', 'wb') as b:
                    writer = csv.writer(b)
                    for line, row in enumerate(bottle_list):
                         data = line_to_override.get(line, row)
                         writer.writerow(data)
                    
                
            else:
                print ("\n\tError. Debes elegir una opción correcta.")
                opcion = 0
                
        
        return sesion_activa
    
    
    
    