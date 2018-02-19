# -*- coding: utf-8 -*-

'''
Created on 16 feb. 2018

@author: Ismael
'''

class Pelicula(object):
    '''
    Modelo de película
    '''
    titulo = ""
    fechaEstreno = 0
    genero = ""
    director = ""
    duracion = 0
    

    def __init__(self, titulo, estreno, genero, director, duracion):
        '''
        Constructor
        '''
        self.titulo = titulo
        self.fechaEstreno = estreno
        self.genero = genero
        self.director = director
        self.duracion = duracion
        
    
    def toString(self):
        cadena = "Titulo: "+ self.titulo+ "\nEstreno en: "+ str(self.fechaEstreno)+ "\nGenero: "+ self.genero+ "\nDirector: "+ self.director+ "\nDuracion: "+ str(self.duracion)
        return cadena
        