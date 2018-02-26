# Gestor de aplicación de stream de series

Proyecto de gestión de sistema de stream de series programado en Python para la asignatura de 'Sistemas de gestión empresarial'.

## Guía para colaborar
<br>

<details>
     <summary>¿Qué es git?</summary>
 <p>
	 
Git es un **sistema de control de versiones** (vcs) que permite la colaboración entre programadores de forma simultánea solucionando y facilitando muchísimo la *integración* del código fuente de los contribuidores. Su funcionamiento consiste en la creación de versiones del proyecto llamados *commits*. Los proyectos pueden seguir diferentes *ramas* según la funcionalidad que se esté implementando o el contribuidor que la esté actualizando. Las diferentes ramas pueden fusionarse a otras ramas, o la rama principal *'master'* e integrar las funcionalidades de ambas ramas en una nueva línea troncal. Abajo podéis ver una ilustración de un arbol versiones de Git.

<br>   
<img src="https://i.stack.imgur.com/DOXN0.png" alt="">

  </li>
      </p></details><br>

 <details>
     <summary>Pasos básicos</summary>
 <p>
   
#### Descargarte el proyecto de nuevo
  1. :arrow_down: Abre una terminal en el directorio del workspace e introduce: `git clone https://github.com/ismenc/python-gestor-series` 
  
#### Actualizar si ya lo tienes descargado
  1. :open_file_folder: Abre una terminal en el directorio del proyecto
  2. :heavy_check_mark: Colócate en tu rama mediante `git checkout -b tu-nombre`
  3. :recycle: Descárgate tu última versión con `git pull origin tu-nombre` 
  
#### Subir tus versiones después de trabajar
  1. :memo: Trabaja con eclipse o como lo quieras hacer
  2. :open_file_folder: Abre una terminal en el directorio del proyecto
  3. :heavy_check_mark: Si no lo has hecho, colócate en tu rama mediante `git checkout -b tu-nombre`
  4.  :exclamation: Haz tu nueva version con `git commit -am "Resumen de cambios"` 
  5. :arrow_up: Sube tus versiones con `git push origin tu-nombre` 
  </li>
      </p></details>
	  <br>

## Índice de contenidos

1. [Integrantes](#integrantes)
2. [Estructura del proyecto](#estructura-del-proyecto)

## Integrantes

Los participantes en el proyecto son:
* Ismael Núñez Carrión
* Diego Arroyo García
* Davinia Pineda Bonilla
* Eduardo Muñoz Villalba
* Ricardo Terán

## Estructura del proyecto

<img src="doc/diagrama-clases.png" alt="">

## Desplegable de clases
<br>

<details>
     <summary>Película</summary>
 <p>
	 
Clase que define la estructura de datos de las películas; así como su título, género, director, duración y fecha de estreno.

 </p>
 </details><br> 

<details>
     <summary>Serie</summary>
 <p>
	 
Clase que define la estructura de datos de las series; así como su título, género, fecha de estreno, duración media de los capítulos y número de temporadas hasta la fecha.

 </p>
 </details><br> 
 
 <details>
     <summary>Usuario</summary>
 <p>
	 
Clase que almacena los datos del usuario; así como su nombre, clave, edad y dos arrays para guardar tanto las series o películas vistas como las marcadas en pendientes de ver. Tambien dispone de unos métodos para añadir dichas series o películas a sendos arrays o visualizar el contenido de estos.
Se han realizado controles para evitar introducir más de una vez, la misma serie o película, en los metodos para añadir a visto o marcar como pendiente.

 </p>
 </details><br> 
 
 <details>
     <summary>_init_</summary>
 <p>
	 
Principal donde ejecutamos todas las acciones.

 </p>
 </details><br> 
 
 <details>
     <summary>Util</summary>
 <p>
	 
Clase que provee a la principal de los métodos estáticos para interactuar con el usuario y gestionar los objetos.
* loguear(user, password) - nos permite logearnos si el usuario está en la base de datos o lo registra si no está
* mostrar_menu() - muestra el menú con las opciones por pantalla
* tratar_menu() - función que resuelve toda la casuística correspondiente a la opción elegida por el usuario
* leerEntero() - solicita un número entero que sea validado
* cargarCatalogoPeliculas() - carga las películas en el fichero X en memoria
* cargarCatalogoSeries() - carga las series en el fichero X en memoria
* mostrarLista(msg, lista) - muestra por pantalla el mensaje y a continuación la lista de películas o series que le pasemos

 </p>
 </details>
