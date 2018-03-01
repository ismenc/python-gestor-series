# -*- coding: utf-8 -*-


class Usuario:
    '''
    Clase que define la estructura de datos del usuario
    '''
    nombre = ""
    clave = ""
    edad = 0
    visto = []
    pendienteVer = []

    def __init__(self, nombre, clave, edad):
        if(edad < 16 or edad > 90):
            raise ValueError("Edad no válida")
        
        self.nombre = nombre
        self.clave = clave
        self.edad = edad
        
        
    ''' Métodos para añadir a las listas '''

    def addAVisto(self, serieOPelicula):
        # Validamos que no esté ya en visto
        if serieOPelicula not in self.visto:
            self.visto.append(serieOPelicula)
            # Elminamos de pendiente si la hemos visto
            if serieOPelicula in self.pendienteVer:
                self.pendienteVer.remove(serieOPelicula)
                print("Se ha añadido a visto correctamente.")
        else:
            print(serieOPelicula + " ya se encontraba en visto.")

    def addAPendienteVer(self, serieOPelicula):
        # Agregamos si no está en visto
        if serieOPelicula not in self.visto:
            # Validamos que no esté ya en pendiente
            if serieOPelicula not in self.pendienteVer:
                self.pendienteVer.append(serieOPelicula)
                print("Se ha añadido a pendientes correctamente.")
            else:
                print(serieOPelicula + " ya se encontraba en pendientes.")
        else:
            print(serieOPelicula + " ya se ha visto y no se puede añadir a pendiente")
            
            
    ''' Métodos para mostrar por pantalla '''
            
    def verVisto(self):
        # Validamos que haya visto algo
        if len(self.visto) == 0:
            print(self.nombre+ " no ha visto nada todavía.")
        else:
            print ("Las películas y series que "+ self.nombre+ " ha visto son: \n* " + "\n* ".join(self.visto))

    def verPendientes(self):
        #validamos que se hayaañadido algo a pendiente
        if len(self.pendienteVer) == 0:
            print(self.nombre+ " no ha añadido nada a pendiente todavía.")
        else:
            print ("Las películas y series que "+ self.nombre+ " tiene pendientes son: \n* " + "\n* ".join(self.pendienteVer))

