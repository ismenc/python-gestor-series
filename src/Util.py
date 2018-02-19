# -*- coding: utf-8 -*-


class Util():

    @staticmethod
    def tratarUsuario(archivo, datos_usuario):

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
