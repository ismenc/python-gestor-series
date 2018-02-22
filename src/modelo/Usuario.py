# -*- coding: utf-8 -*-


class Usuario:
    nombre = ""
    clave = ""
    edad = 0
    visto = []
    pendienteVer = []

    def __init__(self, nombre, clave, edad):
        self.nombre = nombre
        self.clave = clave
        self.edad = edad

'''
    def addAVisto(self, serieOPelicula):
        if serieOPelicula not in visto:
            self.visto.append(serieOPelicula)
        else:
            print "Ya se encuentra en la lista."

    def addAPendienteVer(self, serieOPelicula):
        if serieOPelicula not in pendienteVer:
            self.pendienteVer.append(serieOPelicula)
        else:
            print "Ya se encuentra en la lista."

    def verVisto(self):
        print ("Las peliculas y series que has visto son: " + ", ".join(visto))

    def verPendientes(self):
        print ("Las peliculas y series que tienes pendiente son: " + ", ".join(pendienteVer))

''' 
    #Funcion que guarde pelicula en fichero
