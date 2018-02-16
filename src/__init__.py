# -*- coding: utf-8 -*-
from formatter import NullFormatter

archivo = open("Usuarios.txt", "a+")

nombre_usuario = raw_input("Introduce tu nombre de usuario: ")
password = raw_input("Introduce tu contraseña: ")

datos_usuario = nombre_usuario+ ", "+password

linea = archivo.readline()
while linea != "fin":
    print linea
    linea = archivo.readline()
    #usar metodo linea.find() para encontrar la posicion de la , y partir la cadena

#archivo.write("\n"+datos_usuario)