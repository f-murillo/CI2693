import math # Importar math para calcular la distancia entre puntos 

def distancia(p1, p2):
    """Método que calcula la distancia entre dos puntos"""
    x1, y1 = p1
    x2, y2 = p2
    res1 = math.pow(x2-x1,2)
    res2 = math.pow(y2-y1,2)
    return math.sqrt(res1 + res2) 

class CustomMinHeap:
    """Clase que implementa una cola de prioridad (min heap)"""
    def __init__(self):
        self.heap = []

    def push(self, v, cost):
        """Método que agrega un elemento con su costo al heap"""
        self.heap.append((v, cost))
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Método que elimina el elemento con menor costo, y llama a heapify_down para asegurarse de mantener las propiedades del min heap"""
        if not self.heap:
            return None
        v, _ = self.heap[0]  
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return v

    def update(self, v, new_cost):
        """Método que actualiza el costo de un elemento, y llama a heapify_up para asegurarse de mantener las propiedades del min heap"""
        for i, (vertex, _) in enumerate(self.heap):  
            if vertex == v:
                self.heap[i] = (v, new_cost)
                self._heapify_up(i)
                break

    def __contains__(self, v):
        """Permite verificar si un elemento está en el heap"""
        return any(vertex == v for vertex, _ in self.heap)

    def __len__(self):
        """Retorna el numero de elementos del heap"""
        return len(self.heap)

    def _heapify_up(self, i):
        """Método que se usa al actualizar un elemento para mantener la propiedades del min heap"""
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][1] < self.heap[parent][1]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
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

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)


def prim(conjuntos_residenciales, central_internet):
    """Algoritmo de Kruskal que retorna un árbol mínimo cobertor y su costo
    
    Entrada: Lista de tuplas (conjuntos residenciales), y una tupla adicional (central)
    Salida: Lista de pares de tuplas (lista de lados) que representa el árbol mínimo cobertor; y el costo total del árbol
    """
    # Agregar central a lista (para poder trabajarlo)
    conjuntos_residenciales.append(central_internet)
    n = len(conjuntos_residenciales)
    h = CustomMinHeap()
    res = [] # Donde se irán guardando los índices de los vértices
    c = {} # Donde irán los costos
    parents = {} # Padres
    total_cost = 0 # Costo del árbol

    # inicializar padres en nulo, costos en infinito y agregar al heap vértices y sus costos
    for v in range(n):
        c[v] = float('inf')
        parents[v] = None
        h.push(v, c[v])

    # Se tomará por defecto el primer vértice
    c[0] = 0
    h.update(0, c[0])

    # Mientras el heap no esté vacío
    while h:
        v = h.pop() # Desencolar elemento de menor costo
        res.append((parents[v], v)) # Agregar elemento desencolado y su padre
        total_cost += c[v] # Agregar costo al costo final
        for i in range(n): # Para todos los adyacentes al vértice desencolado
            if i != v and i in h:  
                # Si la distancia de v a i es menor al costo de i, se actualiza el costo de i a w, y el padre de i pasa a ser v. Y actualiza el heap
                w = distancia(conjuntos_residenciales[v], conjuntos_residenciales[i])
                if w < c[i]:
                    c[i] = w
                    parents[i] = v
                    h.update(i, c[i])

    # Recuperar las coordenadas de los conjuntos residenciales, y devolver resultados
    mst = [(conjuntos_residenciales[u], conjuntos_residenciales[v]) for u, v in res if parents[v] is not None]
    return mst, total_cost


