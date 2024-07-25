# Laboratorio 2: DFS, BFS y Backtracking

# Integrantes

- Franco Murillo 16-10782
- Eliezer Cario 18-10605
- Fredthery Castro 18-10783

# Problemas

* Problema1.py
    - Resuelve el problema de encontrar un camino en un laberinto 2D (matriz a*b con ceros y unos, donde un 1 representa una pared, y un 0 representa un camino libre) usando DFS recursivo
    - Se puede definir un grafo implícito (no hace falta declarar ningún grafo en el código) G = (V,E), donde:
        - V: celdas del laberinto (matriz)
        - E: los lados (x,y), (con x,y en V) tal que x es adyacente a y (arriba, abajo, izquierda o derecha), 
             y el valor de la celda x y la celda y es 0 (me puedo mover de x a y)
    - Consta de 3 métodos:
        1- DFS_Laberinto: Es el método principal que se llama al ejecutar el programa, y que llama al método recursivo
                         por primera vez 
            Entradas: un laberinto, un punto inicial y un punto final
            Salida: una lista de tuplas que representa el camino encontrado entre los dos puntos. Si no se encuentra un camino, retorna None
            Complejidad: O(|V| + |E|) (la complejidad del método recursivo)

        2- DFS_Recursivo: Es el método que se encarga de resolver el problema de manera recursiva
            Entradas: un laberinto, el punto actual, el punto final, un conjunto de puntos visitados y el camino acumulado hasta ese momento
            Salida: True si el camino pasado efectivamente llega hasta el final, o False en caso contrario
            Complejidad: O(|V| + |E|)

        3- obtener_vecinos: Es el método que se encarga de obtener las celdas a las que me puedo mover desde una celda dada
            Nota: La forma en la que se agregan los vecinos genera el orden de exploración de DFS: abajo, derecha, izquierda, arriba
            Entradas: un laberinto, y una posición de celda
            Salida: Una lista de tuplas con los vecinos de la celda dada
            Complejidad: O(1), ya que siempre se verifican 4 posiciones a partir de la celda dada (arriba, abajo, izquierda y derecha)
    - Luego, la complejidad total del algoritmo es O(|V| + |E|)

* Problema2.py
    - Resuelve el problema de encontrar el camino más corto entre dos vértices de un grafo G = (V,E) implementado con una lista de adyacencias usando el recorrido BFS. Al hacer el recorrido usando BFS, nos aseguramos que el camino devuelto sea el más corto
    - Consta de 1 método:
        1- BFS: es el método que resuelve el problema
            Entradas: un grafo, un vértice de salida y un vértice de llegada
            Salida: el camino más corto entre los dos vértices
            Complejidad: O(|V| + |E|), ya que recorre cada vértice y cada lado exactamente una vez
    - Luego, la complejidad total del algoritmo es O(|V| + |E|)

* Problema3.py
    - Resuelve el problema de las N-Reinas usando DFS recursivo   
    - Consta de 3 métodos:
        1- DFS_N_Reinas: Es el método principal que se llama al ejecutar el programa, y que llama al método recursivo por primera vez
            Entrada: un n que representa el tamaño del tablero (nxn), y el número de reinas a colocar
            Salida: una lista de listas, donde cada lista interna tiene una solución con las posiciones donde se puede colocar las reinas
            Complejidad: O(n!) (la complejidad del método recursivo)

        2- DFS_Recursivo: Es el método que resuelve el problema de manera recursiva
            Entradas: n, una fila, una posición y la lista de soluciones que se tiene hasta el momento
            Salida: Lista de listas con las soluciones posibles
            Complejidad: O(n!), pues en el peor de los casos, el algoritmo verificaría todas las soluciones posibles antes de encontrar alguna solución válida

        3- es_Seguro: Es el método que verifica si es seguro colocar o no una reina en una casilla
            Entradas: Una lista con las posiciones donde se encuentras las reinas colocadas hasta el momento, la fila donde se quiere colocar la nueva reina, y la columna donde se quiere colocar la nueva reina
            Salida: True si se puede colocar una reina en la casilla, o False en caso contrario
            Complejidad: O(n) ya que en el peor caso se tendría que verificar las n reinas para saber si es seguro colocar la nueva reina

    - Luego, la complejidad total del algoritmo es O(n!) 

* Problema4.py
    - Resuelve el problema de encontrar el camino más corto entre dos puntos de un laberinto 2D (matriz a * b con ceros y unos, donde un 1 representa una pared, y un 0 representa un camino libre) con obstáculos móviles 
    - Se usó el recorrido BFS para resolver el problema
    - Consta de 1 método:
        BFS_Laberinto: Es el método que resuelve el problema
        Entradas: un laberinto, el punto de salida, el punto de llegada, y una lista de obstáculos móviles con su ruta
        Salida: lista de tuplas que representa el camino más corto encontrado entre los dos puntos. Si no se encontró ningún camino, retorna None
        Complejidad: O((n^2)*m), donde n = a * b (número de celdas), y m es el número de obstáculos móviles. Esto es porque en el peor caso cada celda puede ser visitada n veces, por los obstáculos móviles. Además, para cada celda visitada, se verifican los m obstáculos móviles para saber si la celda es segura
    - Luego, la complejidad total del algoritmo es O((n^2)*m)

* test_Lab2.py
    - Realiza los tests unitarios para dada archivo 
    - Hace uso de la clase unittest
    - Para cada archivo se usaron 2 casos de prueba
        



