# Quiz 1. Franco Murillo 16-10782

# Buscador de Caminos más cortos en la Universidad

Este algoritmo resuelve el problema de encontrar el camino más corto en un mapa de una universidad, evitando las zonas de protesta.

El algoritmo toma como entrada un mapa de la universidad representado como una lista de aristas, un punto de inicio, un punto final y una ruta de protesta. El algoritmo busca todos los caminos posibles desde el punto de inicio hasta el punto final, evitando los nodos que están en la ruta de la protesta. Si encuentra un camino que es más corto que el camino más corto actual, actualiza el camino más corto. Al final, devuelve todos los caminos más cortos encontrados

## Complejidad Temporal

La complejidad temporal del algoritmo es O(N!), donde N es el número de nodos en el grafo. Esto se debe a que en el peor de los casos, el algoritmo tiene que explorar todos los posibles caminos en el grafo, lo cual en el número de nodos. es factorial 

