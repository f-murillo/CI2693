import math
class CustomMinHeap:
    """Clase que implementa una cola de prioridad (min heap)"""
    def __init__(self):
        self.heap = []  # Lista para almacenar los elementos (vértices y costos)
        self.vertex_to_index = {}  # Diccionario para mapear vértices a índices (Para tener un tiempo de busqueda constante)

    def push(self, v, cost):
        """Método que agrega un elemento con su costo al heap"""
        self.heap.append((v, cost))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Método que elimina el elemento con menor costo, y se asegura de mantener las propiedades del min heap"""
        if not self.heap:
            return None
        v, _ = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return v

    def update(self, v, new_cost):
        """Método que actualiza el costo de un elemento, y se asegura de mantener las propiedades del min heap"""
        if v in self.vertex_to_index:
            i = self.vertex_to_index[v]  # Obtenemos el índice del vértice
            if 0 <= i < len(self.heap):
                self.heap[i] = (v, new_cost)
                self._heapify_up(i)
                self._heapify_down(i)
            else:
                raise ValueError(f"El índice {i} está fuera de los límites del heap")
        else:
            raise ValueError(f"El vértice {v} no está en el heap")

    def __contains__(self, v):
        """Permite verificar si un elemento está en el heap"""
        return v in self.vertex_to_index

    def __len__(self):
        """Retorna el numero de elementos del heap"""
        return len(self.heap)

    def _heapify_up(self, i):
        """Método que se usa al actualizar un elemento para mantener la propiedades del min heap"""
        while i > 0:
            parent = (i - 1) // 2
            # Si el elemento es menor al padre, intercambiar 
            if self.heap[i][1] < self.heap[parent][1]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                self.vertex_to_index[self.heap[i][0]] = i
                self.vertex_to_index[self.heap[parent][0]] = parent
                i = parent
            else:
                break

    def _heapify_down(self, i):
        """Método que se utiliza al eliminar un elemento para mantener la propiedades del min heap"""
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i

        if left_child < len(self.heap) and self.heap[left_child][1] < self.heap[smallest][1]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child][1] < self.heap[smallest][1]:
            smallest = right_child
            
        # Si smallest es distinto de i, intercambiar elementos 
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i] 
            self.vertex_to_index[self.heap[i][0]] = i
            self.vertex_to_index[self.heap[smallest][0]] = smallest
            self._heapify_down(smallest)

            
def time_adjusted(distance, initial_v, slope):
    """ Metodo que calcula el tiempo de viaje ajustado (teniendo en cuenta la pendiente de la carretera)

    Args:
        distance (float): La distancia a recorrer.
        initial_v (float): La velocidad inicial.
        slope (float): La pendiente de la carretera en grados.

    Returns:
        float: El tiempo de viaje ajustado.

    Raises:
        ValueError: Si la pendiente es de 90 grados o -90 grados.

    """
    # Transformar la pendiente de grados a radianes
    if slope == 90 or slope == -90:
        raise ValueError("The slope cannot be 90 degrees.")
    pen = (slope * math.pi) / 180

    # Calcular la velocidad ajustada (tomando en cuenta la pendiente)
    adjusted_velocity = initial_v * math.cos(pen)

    # Calcular el tiempo de viaje ajustado
    return distance / adjusted_velocity
            
def dijkstra_gas_consumption(road_network, start_city, end_city, initial_velocity, gasoline_consumption_per_km, initial_gasoline, max_time_extension_factor):
    """
    Método que implementa el algoritmo de Dijkstra para calcular el consumo de gasolina de la ruta óptima entre dos ciudades
    y el tiempo que toma realizar el viaje.

    Args:
        road_network (dict): Un diccionario que representa la red de carreteras, donde las claves son las ciudades y los valores son listas de tuplas que contienen información sobre las ciudades vecinas, la distancia entre ellas y la pendiente de la ruta.
        start_city (str): La ciudad de inicio.
        end_city (str): La ciudad de destino.
        initial_velocity (float): La velocidad inicial del viaje en km/h.
        gasoline_consumption_per_km (float): El consumo de gasolina por kilómetro en litros.
        initial_gasoline (float): La cantidad inicial de gasolina en litros.
        max_time_extension_factor (float): El factor máximo de extensión de tiempo permitido.

    Returns:
        tuple: Una tupla que contiene el costo total de gasolina consumida en el viaje y el tiempo total de viaje ajustado.

    Note:
        El tiempo de viaje ajustado tiene en cuenta la pendiente de la ruta y el tiempo ideal de viaje.

    """
    cities = list(road_network.keys()) # Lista de ciudades
    inf = float('inf') # Costo inicial de las ciudades (menos la inicial)
    cost = {city: inf for city in cities} # Diccionario de costos
    cost[start_city] = 0 # Costo de la ciudad inicial
    pq = CustomMinHeap() # Cola de prioridad

    pq.push(start_city, 0)  # Agregar la ciudad de inicio a la cola con costo cero
    time = 0  # Acumulador del tiempo de viaje de la ciudad inicial a la final

    # Mientras la cola no esté vacía
    while pq:
        u = pq.pop() # Desencolar elemento con menor costo
        # Si ya se llegó a la ciudad destino, salir del ciclo
        if u == end_city:
            break
        
        # Para cada ciudad, con su distancia y su pendiente de la ruta de ciudades
        for w, distance, slope in road_network[u]:
            # Calcular tiempo de viaje ideal
            travel_time = distance / initial_velocity
            # Calcular tiempo ajustado a la pendiente
            travel_time_adjusted = time_adjusted(distance, initial_velocity, slope)
            # Calcular consumo de gasolina entre ciudades
            gas_consumption = (distance * gasoline_consumption_per_km) * ( 1 + (slope / 100) )
            # Si el consumo de gasolina es menor a la gasolina que se tiene, y el tiempo ajustado es menor o igual al tiempo ideal con el factor de extension maximo
            if (gas_consumption < initial_gasoline) and (travel_time_adjusted <= travel_time * max_time_extension_factor):
                # Si el costo de u + el consumo de gasolina de ir de u a w es menor al costo de w
                if cost[u] + gas_consumption < cost[w]:
                    cost[w] = cost[u] + gas_consumption # Actualizar costo de w
                    # Si w está en la cola, se actualiza su costo. Si no está en la cola, se agrega con su costo
                    if w in pq:
                        pq.update(w, cost[w])
                    else:
                        pq.push(w, cost[w])
                    # Agregar tiempo de viaje ajustado al acumulador, y restar el consumo de gasolina a la gasolina que se tiene  
                    time += travel_time_adjusted
                    initial_gasoline -= gas_consumption

    # Si el costo de la ciudad final es infinito, no se encontró forma de llegar. Retornar None,None
    if cost[end_city] == inf:
        return None, None
    # Si el costo es distinto de infinito, retornar el costo y el tiempo acumulado
    return cost[end_city], time
