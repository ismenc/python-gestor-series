# -*- coding: utf-8 -*-

import Pelicula as p
import Usuario as u

usuario = u.Usuario("Edu", "qwe", 22)
print (usuario.nombre)
print (usuario.edad)

peli = p.Pelicula("Star wars", 1980, "Sci-fi", "Lucas noseke", 108)
peli2 = p.Pelicula("Monsters SA", 2005, "Infantil", "Uno de 2hermana", 77)
peli3 = p.Pelicula("Diarrea", 2018, "fantasía", "yo", 9999999)

visto = [peli.titulo, peli2.titulo, peli3.titulo]
print ("Las peliculas son: " + ", ".join(visto))

#Probar series. El toString de series tal vez no esté bien
>>>>>>> .merge_file_a03052
