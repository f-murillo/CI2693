# Laboratorio 4: Camino Óptimo entre ciudades

Integrantes:
- Franco Murillo 16-10782
- Eliezer Cario 18-10605
- Fredthery Castro 18-10783


Se desea calcular un camino de consumo de gasolina y tiempo óptimos, dados:
- Una red de Carreteras
- Pendiente de las carreteras (que pueden ir de -90 a 90)
- Consumo de Gasolina, que se ajusta por el grado de la pendiente de la carretera
- Velocidad Inicial en km/h
- Gasolina Inicial en litros
- Ciudad inicial
- Ciudad destino
- Un factor de extensión máxima de tiempo de viaje entre ciudades

Si se modelase el problema usando un grafo:

- Los vértices son las ciudades
- Los lados son las carreteras entre ciudades, donde cada lado tiene asociado un costo en consumo de gasolina

Luego, para resolver el problema, se usará el algoritmo de Dijkstra.

Además, se desea considerar que en algunas ciudades dadas de la red, se tenga recarga de gasolina gratis, lo que implica
un consumo negativo de gasolina. Para este caso se usará el algoritmo de Bellman. 

# Dijkstra
- Se implementó una cola de prioridad usando un min heap, en la clase CustomMinHeap, el cual usa una lista para almacenar los 
vértices y sus costos, y además un diccionario para almacenar los índices de los vértices, para poder ubicarlos en tiempo constante.

- Los métodos de la clase CustomMinHeap son:
    - `push` : agrega un elemento a la cola, y se asegura de mantener las propiedades del heap. Complejidad: O(log(n))
    - `pop` : desencola el elemento de menor costo, y se asegura de mantener las propiedades del heap: Complejidad: O(log(n))
    - `update` : busca el elemento en la cola, actualiza el costo del vértice, y se asegura de mantener las propiedades del heap. Complejidad: O(log(n))
    - `contains` : verifica si un elemento está en la cola. Complejidad: O(1)
    - `len` : retorna la longitud del heap. Complejidad: O(1)
    - `heapify_up` : compara el elemento actual con su padre, y en caso de ser menor, va intercambiando los elementos. Complejidad: O(log(n))
    - `heapify_down` : compara el elemento actual con sus hijos, y en caso de ser menor a alguno de ellos, va intercambiando los elementos. Complejidad: O(log(n))

- Se implementó una función que calcula el tiempo de viaje entre ciudades tomando en cuenta la pendiente de la carretera (`time_adjusted`)
    - Entrada:
      - distancia entre las ciudades (dada en la red de carreteras)
      - velocidad inicial
      - pendiente de la carretera
    - Salida:
      - tiempo de viaje ajustado a la pendiente
    - Primero, verifica que la pendiente no sea exactamente 90 o -90, pues esos valores no tendrían sentido físico (Es decir, 90 sería como escalar una pared y -90 como caer por un acantilado), además de que por el tipo de cálculo usado darían como resultado una división entre 0.
    - Para calcular el tiempo, se usa la fórmula: `tiempo = distancia / velocidad`
    - Como se cuenta con una pendiente x, la velocidad viene dada por: `velocidad = velocidad_inicial * cos(x)`
    - Pero el problema define la pendiente en grados, por lo que primero es transformado a radianes antes de calcular el coseno, usando la fórmula: `radianes = (x° * pi) / 180°`
    - Para usar pi, y para calcular el coseno, se hace uso del módulo math de Python
    - Ya con la velocidad calculada, se retorna el valor de la distancia dividida entre esta velocidad
- **Algoritmo de Dijkstra** :
    - Se inicializan la lista con las claves de las ciudades y un diccionario de costos por ciudad, todos con infinito
    - Se establece el costo de la ciudad inicial en cero
    - Se crea la cola de prioridad, y se agrega la ciudad inicial con su costo
    - Se declara el acumulador del tiempo del camino óptimo en cero
    - Se itera mientras la cola no esté vacía:
        - Se desencola el elemento "u" de menor costo
        - Si u es la ciudad destino, ya llegamos, por lo que se sale del ciclo
        - Si no, se itera por cada ciudad (con su distancia y pendiente) "w" que aparece en la lista de adyacentes de u
            - Se calcula el tiempo ideal de viaje (sin tomar en cuenta la pendiente de la carretera)
            - Se calcula el tiempo ajustado a la pendiente (con la función time_adjusted)
            - Se calcula el consumo de gasolina, tomando en cuenta el consumo de gasolina por km, la distancia entre las ciudades, y la pendiente de la carretera
            - Si el consumo de gasolina calculado es menor a la gasolina que se tiene hasta ese momento, y además el tiempo ajustado calculado es menor o igual al tiempo ideal con el factor de extensión máximo:
                - Si el costo de u más el consumo de gasolina calculado es menor al costo de w:
                    - Se establece como nuevo costo de w el costo de u más el consumo de gasolina calculado
                        - Si está, se actualiza su costo en la cola
                        - Si no está, se agrega a la cola con su costo
                    - Luego se suma el tiempo ajustado calculado al acumulador del tiempo, y se resta a la gasolina que se tiene hasta el momento el consumo de gasolina calculado
    - Al terminar el ciclo, se verifica el costo de la ciudad destino:
        - Si su costo es infinito, no se halló un camino desde la ciudad inicial hasta el destino, por lo que se retorna None, None
        - Si su costo es distinto de infinito, se halló un camino desde la ciudad inicial, por lo que se retorna el costo del destino, y el tiempo acumulado del viaje

- **Complejidad de Dijkstra** :
    - La función `time_adjusted` es O(1)
    - Se accede a cada ciudad (vértice) una vez. Si llamamos n al número de vértices, esto es O(n)
    - Se accede a cada adyacente de cada ciudad una vez (a cada lado una vez). Si llamamos m al número de lados, esto es O(m)
    - Se actualiza o se agrega a la cola de prioridad en el peor caso m veces. Tanto agregar como actualizar son O(log(n)), por lo que la complejidad de agregar o actualizar en el ciclo es O(m * log(n))
    - Finalmente, la complejidad total es O(m * log(n)), donde m es el número de lados, y n el número de vértices      

# Bellman
- La entrada del programa es el mismo, pero se agrega una lista de ciudades donde se cuenta con recarga gratuita de gasolina
- El enfoque es parecido al de Dijkstra, pero usando fuerza bruta (recorriendo todos los lados posibles de la red de carreteras)
- Como se van a verificar todos los lados, no se utiliza la cola de prioridad
- Se sigue utilizando la función `time_adjusted` para calcular el tiempo tomando en cuenta la pendiente
- Inicializa las variables a usar igual que en Dijkstra: lista con claves de las ciudades (pero aquí obtiene la longitud de la lista en n), diccionario de costos con infinito,y establece el costo de la ciudad inicial en cero
- Se declara el acumulador del tiempo en cero
- Se itera n-1 veces (con ciclo for):
    - Dentro del ciclo for, se itera para cada ciudad "city" en la lista de claves de ciudades
        - Si city es la ciudad destino, se sale del ciclo
        - Si no, se itera por cada ciudad (con su distancia y pendiente) "w" que aparece en la lista de adyacentes de city:
            - Se calcula el tiempo ideal, el tiempo ajustado y el consumo de gasolina igual que en Dijkstra
            - Se verifica si w está en la lista de ciudades de recarga gratuita de gasolina
                - Si está, se multiplica el consumo de gasolina calculado por -1                                       
            - Si el consumo de gasolina calculado es menor a la gasolina que se tiene hasta ese momento, y además el tiempo ajustado calculado es menor o igual al tiempo ideal con el factor de extensión máximo:
                - Si el costo de city más el consumo de gasolina calculado es menor al costo de w:
                    - Se establece como nuevo costo de w el costo de u más el consumo de gasolina calculado
                    - Se suma el tiempo ajustado calculado al acumulador del tiempo, y se resta a la gasolina que se tiene hasta el momento el consumo de gasolina calculado
- Al salir del ciclo for, se vuelve a iterar para cada ciudad city para verificar que no haya ciclos negativos:
    - Se itera para cada w que aparece en la lista de adyacentes de city
        - Se calcula el consumo de gasolina
        - Si el costo de city más el consumo calculado es menor al costo de w (luego del ciclo anterior) y el costo es distinto de infinito:
            - Se encontró un ciclo negativo, por lo que se retorna el error
- Finalmente, al igual que con Dijkstra, se verifica si el costo de la ciudad destino es infinito o no:
    - Si es infinito, no se encontró camino
    - Si no es infinito, se retorna el costo y el tiempo acumulado

- Complejidad de Bellman:
    - La función `time_adjusted` es O(1)
    - Se itera n-1 veces, donde n es el número de vértices, esto es O(n)
    - Se itera sobre todos los lados posibles, donde m es el número de lados. Esto es O(m)
    - Finalmente, la complejidad de `Bellman` es O(n * m)               
    

    
