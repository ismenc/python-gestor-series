# -*- coding: utf-8 -*-

'''
	Modelo de Serie
Created on 22 feb. 2018
@author: Ismael
'''

class Serie(object):
    '''
    Modelo de serie
    '''
    titulo = ""
    fechaEstreno = ""
    genero = ""
    director = ""
    duracion = 0
    temporadas = []

    # Constructor
    def __init__(self, titulo, fechaEstreno, genero, director, duracion, temporadas):
        self.titulo = titulo
        self.fechaEstreno = fechaEstreno
        self.genero = genero
        self.director = director
        self.duracion = duracion
        self.temporadas = temporadas

    def toString(self):
        cadena = "Serie: "+ self.titulo+ "\nEstreno en: "+ str(self.fechaEstreno)+ "\nGénero: "+ self.genero + "\nDirector: "+ self.director + "Duracion(capítulos): " + str(self.duracion) + "\nCapítulos por cada temporada: \n" + ", ".join(self.temporadas)
        return cadena

    #Funcion que guarde serie en fichero
