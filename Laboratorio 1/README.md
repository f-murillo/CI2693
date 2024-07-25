# Laboratorio 1

# Hecho por: Franco Murillo - 1610782

# Ejercicio1.py
- Contiene la implementación de las dos versiones del algoritmo de Roy-Warshall para calcular la matriz de alcance de un grafo implementado con una matriz de adyacencias.

# Ejercicio2.py
- Contiene la implementación del algoritmo que calcula las componentes conexas de un grafo implementado con una matriz de adyacencias.
- Hace uso del algoritmo que calcula la matriz de alcance de Ejercicio1. En particular, se usa la 2da versión de Roy-Warshall.

# Ejercicio3.py
- Contiene la implementación de un algoritmo que calcula los puntos de articulación de un grafo implementado con una matriz de adyacencias.
- Hace uso del algoritmo que calcula las componentes conexas de Ejercicio2.

# Ejercicio4.py
- Contiene la implementación de un algoritmo que genera un informe de una red social simulada (representada con un grafo, implementado con una matriz de adyacencias) y lo guarda en un archivo de tipo .txt
- Hace uso de las funciones de Ejercicio1, Ejercicio2 y Ejercicio3.

# test_Lab1_v1.py y test_Lab1_v2.py
- Ambos archivos contienen los test para cada uno de los archivos anteriormente mencionados
- La versión 1 hace los test manualmente, imprimiendo los resultados esperados y los obtenidos
- La versión 2 hace uso de unittest para realizar los tests
- Los tests se realizaron en un solo archivo (para cada versión), ya que se consideró que los códigos no eran tan extensos o complejos como para dedicarles un archivo de test a cada uno.

   *DESCRIPCION SOBRE LOS TEST DE LOS EJERCICIOS 1, 2 Y 3*
   Se usaron para los tests ejemplos vistos tanto en las clases de teoría de Algoritmos y Estructuras 3, como vistos en internet
  
   *DESCRIPCION SOBRE EL TEST DEL EJERCICIO 4*
   La red social a simular será una al estilo de Facebook, donde si el usuario A es amigo del usuario B, entonces el usuario
    B es amigo del usuario A. Además, si A es amigo de B, y B es amigo de C, entonces A aparecerá como un potencial amigo de C
    y viceversa. Así, el grafo que representa esa situación tendrá como componentes conexas aquellos grupos donde todo usuario
    es amigo o potencialmente amigo del resto de usuarios de dicho grupo. 
    
    En el ejemplo planteado, la red social cuenta con 9 usuarios (acaba de ser lanzada) numerados del 0 al 8. El Algoritmo 
    genera un informe que muestra:
    
    - Cuál es la matriz de adyacencias correspondiente a los 9 usuarios
    - Cuál es la matriz de alcance (qué usuarios son potencialmente amigos de otros usuarios)
    - Cuáles son las componentes conexas (qué grupos de amigos se han formado)
    - Cuáles son los puntos de articulación (qué usuarios mantienen los grupos de amigos unidos)