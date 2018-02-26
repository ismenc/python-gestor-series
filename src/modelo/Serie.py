# -*- coding: utf-8 -*-

'''
	Modelo de Serie
Created on 22 feb. 2018
@author: Ismael
'''

class Serie(object):
    titulo = ""
    fechaEstreno = ""
    genero = ""
    director = ""
    duracion = ""
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
        cadena = "Serie: "+ self.titulo+ "\nEstreno en: "+ str(self.fechaEstreno)+ "\nGénero: "+ self.genero + "\nDirector: "+ self.director+ "\nDuracion: "+ str(self.duracion) + "\nTemporadas: " + self.temporadas
        return cadena

    #Funcion que guarde serie en fichero
