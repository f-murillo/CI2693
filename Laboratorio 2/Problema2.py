# Importar la clase deque (cola de doble extremo)
from collections import deque

def BFS(grafo, inicio, fin):
    """Método que resuelve el problema del camino más corto entre dos vértices de un grafo usando BFS"""
    # Crear un conjunto y agregar el nodo de inicio a los nodos visitados
    visitados = {inicio}  
    # Crear una cola y agregar el nodo de inicio y el camino hasta ahora (que solo contiene el nodo de inicio)
    cola = deque([(inicio, [inicio])])  

    # Mientras la cola no esté vacía
    while cola:  
        # Extraer el primer nodo y el camino hasta ese nodo de la cola
        (nodo, camino) = cola.popleft()
        # Para cada vecino del nodo actual  
        for vecino in grafo[nodo]: 
            # Si el vecino no ha sido visitado 
            if vecino not in visitados:
                # Si el vecino es el nodo final, retornar el camino hasta el nodo actual, más el nodo final 
                if vecino == fin:  
                    return camino + [vecino] 
                # Agregar el vecino a los nodos visitados 
                visitados.add(vecino)
                # Agregar el vecino y el camino hasta el nodo actual, más el vecino a la cola  
                cola.append((vecino, camino + [vecino]))  

    # Si no se encontró un camino hasta el nodo final, retornar None
    return None