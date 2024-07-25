# Laboratorio 3. Prim y Kruskal. Franco Murillo - 1610782

El problema trata de, dadas una lista de tuplas que representan coordenadas (en km) de conjuntos residenciales, y una tupla adicional que representa una central de internet, conseguir la menor cantidad de cable para conectar todas los conjuntos y la central, y obtener cuál sería la configuración de dicha conexión. Si modelamos este problema usando grafos (esto de manera implícita, no hace falta codificar un grafo):

Sea el grafo G = (V,E), donde:
    * V = {(x,y) | (x,y) es la coordenada de un conjunto residencial o de la central de internet}
    * E = {(a,b) en VXV | a está conectada con b}, donde cada arista tiene un costo, en distancia entre los dos puntos
    * Como está definido el problema y el grafo, se trata de un grafo no orientado

Vemos que el problema puede resolverse calculando un árbol mínimo cobertor, y calculando la suma de sus lados. 
Para esto, se usarán dos algoritmos: Prim y Kruskal

# Algoritmo de Prim
- Primero, se cuenta con una función que calcula la distancia entre dos puntos (que se usará para los costos) 

- Hace uso de una cola de prioridad

- No se puede usar el módulo de Python heapq, el cual ya implementa una cola de prioridad, pues para Prim es necesario actualizar los elementos del heap, lo cual no se puede hacer con heapq

- Por lo que se tuvo que implementar una cola de prioridad (CustomMinHeap), cuyos métodos son:
    * push:
        - Agrega un elemento al heap, al final de la lista(complejidad de tiempo O(1)).
        - Luego llama al método _heapify_up, la cual recorre el camino desde el nodo insertado hasta la raíz, comparando y posiblemente intercambiando elementos. En el peor caso, esto es O(log n), donde n es el número de elementos en el heap.
        - Luego, la complejidad total de push es O(log n).
    * pop:
        Elimina el elemento con menor costo (la raíz), con una complejidad de tiempo O(1).
        Luego llama al método _heapify_down, el cual recorre el camino desde la raíz hasta las hojas, comparando e intercambiando elementos según sea necesario. En el peor caso, esto es O(log n).
        Por lo tanto, la complejidad total del método pop es O(log n).
    * update:
        Actualiza el costo de un elemento y luego llama al método _heapify_up.
        La búsqueda del elemento a actualizar tiene una complejidad de tiempo O(n) en el peor caso (donde n es el número de elementos en el heap).
        El método _heapify_up tiene una complejidad de O(log n).
        Por lo tanto, la complejidad total del método update es O(n + log n). 
    * len:
        Retorna la longitud del heap (número de elementos). Esto tiene una complejidad de tiempo O(1)
    * contains: 
        Retorna true si un elemento está en el heap o false en caso contrario. Como busca en todos los elementos del heap, la complejidad es O(n)

- El algoritmo está basado en el visto en clases

- Declara las variables a usar (número de conjuntos residenciales, resultado final, heap, padres, costo)

- Para cada conjunto residencial, inicializa su padre en None, su costo en infinito, y agrega al heap el conjunto y el costo
    * Esto lo hace en tiempo O(n * log n)

- Luego de manera arbitraria, se escogió el primer conjunto como el punto de partida

- Mientras el heap no esté vacío:
    * Elimina del heap el conjunto v con menor costo (esto lo hará en tiempo O(n * log n))
    * Agrega el padre de v y a v al resultado, y suma el costo de v al acumulador de costo
    * Luego, para el resto de conjuntos residenciales:
        * Calcula la distancia entre el v y el conjunto actual del ciclo
        * Si esta distancia es menor al costo del conjunto actual del ciclo, se actualiza el costo y el padre del conjunto, y se actualiza el heap
        * Esta actualización del heap, en el peor caso, lo hará en tiempo O(n * (n-1) * log n). Esto, porque en el ciclo interno, lo hará (n-1) * log n en el peor caso, y el ciclo externo se ejecutara n veces.

- Luego se recuperan de los índices que se encuentran en el arreglo de padres las tuplas para armar los lados del árbol

- Finalmente se retornan la lista de lados recién construida, y el total de costo obtenido

- Luego, la complejidad total del algoritmo de Prim es O(n * (n-1) * log n) = O(n^2 * log n)

# Algoritmo de Kruskal
- Aquí también se cuenta con una función que calcula la distancia entre dos puntos para los costos

- Para Kruskal no hace falta actualizar elementos de la cola de prioridad, por lo que si se puede usar heapq

- Para implementar el algoritmo de Kruskal, se tuvo que implementar la estructura Conjunto Disjunto, cuyos métodos son:
    * init:
        - Establece cada elemento como su propio representante.
        - Establece el rango de cada elemento en cero.
    * find:
        - Encuentra el representante (parent) de un elemento u.
        - Si u no es su propio representante, se ejecuta recursivamente la función, aplicando aplanamiento.
        - En el peor caso, la recursión puede seguir hasta la raíz del conjunto, lo que resulta en una complejidad de tiempo O(log n).
    * union:
        - Une dos conjuntos (representados por u y v respectivamente)
        - Encuentra los representantes de u y v usando el método find (O(log n))
        - Actualiza la estructura, haciendo uso de la unión por rango:
            + Si el rango de u es menor que el rango de v, se establece a v como representante de u.
            + Si el rango de u es mayor que el rango de v, se establece a u como representante de v.
            + Si los rangos son iguales, se elige a u como representante y se incrementa su rango.
        - Luego, la complejidad de union es O(log n)

- El algoritmo está basado en el visto en clases

- Declara las variables a usar (número de conjuntos residenciales, heap, conjunto disjunto) 

- Calcula los costos de los lados, y los agrega juntos con los lados al heap, en un ciclo anidado. Esto lo hace en tiempo O(n * (n * log n)), ya que la función heappush en el ciclo interno se hace en tiempo O(n * log n), y a su vez eso se hace n veces (en el ciclo externo)

- Declara e inicializa el resultado (lista vacía), el número de componentes conexas (que será el número de tuplas), y el costo total (en cero)

- Mientras el número de componentes conexas sea mayor a 1:
    * Desencola el lado con menor costo del heap
    * Verifica si los vértices del lado (los conjuntos) tienen distintos representantes (están en componentes conexas distintas), con la función find. Esto lo hace en tiempo O(log n)
        + Si ese es el caso, las une con el método unión, agrega los conjuntos al resultado, y disminuye en uno el número de componentes conexas. Esto lo hace en tiempo O(log n)

- Finalmente, retorna los resultados obtenidos

- Luego, la complejidad total de Kruskal es O(n * (n * log n)) = O(n^2 * log n)

# Tests
- Se utilizó el módulo unittest
- Se realizaron dos pruebas para cada algoritmo

