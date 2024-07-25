###### Laboratorio 5 - Franco Murillo - 1610782 ######

El problema trata de ayudar a un estudiante a determinar cuántos trimestres le faltan para poder graduarse, asumiendo que puede meter todas las materias posibles por trimestre (asumiremos que cuenta con permiso de créditos permanente)

Podemos definir el problema de la siguente manera: 
• Dado un archivo con la siguiente estructura:
    • Contiene una sección # Requisitos, seguida de líneas con cada materia y sus requisitos en el formato: Materia: Requisito1, Requisito2, ....
    • Luego, hay una línea # Correquisitos, con pares de materias separadas por una coma.
    • Finalmente, hay una línea # Semestre, seguida de las materias que el estudiante está cursando en el trimestre actual o el anterior (si está en vacaciones), separadas por un espacio en blanco.

• Se debe retornar una lista de trimestres, las cuales deben contener las materias a cursar por el estudiante para poder graduarse, tomando en cuenta los requisitos y correquisitos


###### Métodos usados para resolver el problema ######

Los métodos se encuentran en el archivo "orden.py"

# leer_entrada

• Se encarga de leer el archivo, e inicializar las estructuras correspondientes a los requisitos, correquisitos y las materias actuales:
    • Guarda los requisitos en un diccionario:
        • Cada clave será una materia
        • Cada valor será una lista de materias requisitos de la clave
    • Guarda los correquisitos en una lista de tuplas, donde cada tupla es un par de materias correquisitos
    • Guarda las materias actuales en una lista

• Complejidad: O(l), donde l son las líneas del archivo

# construir_grafo

• Se encarga de construir el grafo dados los requisitos y correquisitos para su uso posterior
    • Procesa cada materia y cada correquisito una vez

• Complejidad: O(n + m), donde n es el número de materias, y m el número de requisitos

# partition_by_levels

• Se encarga de realizar el particionamiento por capas del grafo construido

• Complejidad: O(n^2), donde n es el número de nodos (materias) en el grafo. En el peor caso, cada nodo puede ser procesado n veces debido a la eliminación de nodos y la actualización de los requisitos.

# solution

• Se encarga de acoplar las funciones anteriores para resolver el problema

• Complejidad: O(n^2), la complejidad de partition_by_levels

### Tests ###
Se usaron 3 archivos de prueba ("ejemplo1.txt", "ejemplo2.txt" y "ejemplo3.txt") para los tests que se encuentran en el archivo "testsLab5.py"

### Limitaciones ###

• Por una razón desconocida, el algoritmo parece fallar cuando la o las materias actuales del archivo son materias avenzadas en el flujograma de materias

