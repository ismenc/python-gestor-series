# -*- coding: utf-8 -*-
from Util import Util

archivo = open("Usuarios.txt", "a+")

nombre_usuario = raw_input("Introduce tu nombre de usuario: ")
password = raw_input("Introduce tu contraseña: ")

datos_usuario = nombre_usuario+ ", "+password

Util.tratarUsuario(archivo, datos_usuario)