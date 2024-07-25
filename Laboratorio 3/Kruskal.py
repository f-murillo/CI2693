import math # Importar math para calcular la distancia entre puntos 
import heapq # Importar heapq para su uso en el algoritmo de Kruskal

class DisjointSet:
    """Clase que implementa la estructura conjuntos disjuntos"""
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, u):
        """Método que encuentra el representante de u"""
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        """Método que une u y v bajo un mismo representante"""
        u, v = self.find(u), self.find(v)
        if u == v:
            return
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[v] = u
            self.rank[u] += 1
            
def distancia(p1, p2):
    """Método que calcula la distancia entre dos puntos"""
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 
            
            
def kruskal(conjuntos_residenciales, central):
    """Método que implementa el algoritmo de Kruskal, que retorna un árbol mínimo cobertor y su costo
    
    Entrada: Lista de tuplas (conjuntos residenciales) que representan los vértices, y una tupla adicional (central)
    Salida: Lista de pares de tuplas (lista de lados) que representa el árbol mínimo cobertor; y el costo total de los lados del árbol
    """
    # Agregar central a lista (para poder trabajarlo)
    conjuntos_residenciales.append(central)
    n = len(conjuntos_residenciales)
    h = [] # Heap (cola de prioridad)
    ds = DisjointSet(range(n)) # Inicializar conjunto disjunto

    # Agregar costos de aristas al heap
    for u in range(n):
        for v in range(u + 1, n):
            w = distancia(conjuntos_residenciales[u], conjuntos_residenciales[v])
            heapq.heappush(h, (w, u, v))

    res = []        # Donde se irán guardando los lados
    num_comp = n    # El número de componentes conexas es el número de vértices
    total_cost = 0  # Inicializamos el costo total

    while num_comp > 1: # Mientras haya más de una componente conexa
        w, u, v = heapq.heappop(h) # Desencolar arista de menor costo
        
        # Si el representante de u es distinto al de v, unir u y v, sumar el costo del lado, y decrementar en uno num_comp
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            res.append((conjuntos_residenciales[u], conjuntos_residenciales[v]))
            total_cost += w  # Agregamos el peso al costo total
            num_comp -= 1

    # Retornar resultados
    return res, total_cost


