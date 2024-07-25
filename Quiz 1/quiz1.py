class UniversityPathFinder:
    """Clase que resuelve el problema"""
    def __init__(self, edges):
        self.edges = edges # Caminos del mapa
        self.paths = set() # Set de soluciones encontradas
        self.min_path_length = float('inf') # Tamaño mínimo de la solución

    def find_shortest_path(self, start, end, protest_route):
        """Método que resuelve el problema"""
        visited = set()
        path = []
        self.dfs(start, end, visited, path, protest_route, 0)
        return self.paths

    def dfs(self, start, end, visited, path, protest_route, protest_index):
        """Método que resuelve el problema usando DFS recursivo"""
        visited.add(start) # Añadir posicion actual a visitados
        path.append(start) # Añadir posición actual al camino
        # Si llegamos al final y el camino tiene longitud mínima, se establece un nuevo tamaño mínimo,
        # se eliminan los caminos longitud mayor y se agrega ese nuevo camino
        if start == end and len(path) <= self.min_path_length:
            if len(path) < self.min_path_length:
                self.min_path_length = len(path)
                self.paths.clear()
            self.paths.add(tuple(path))
        else:
            # Buscar las tuplas que tengan como origen el espacio actual, y verificar si sus destinos no coinciden con la protesta
            for edge in self.edges:
                if edge[0] == start:
                    next_protest_index = (protest_index + 1) % len(protest_route)
                    if edge[1] not in visited and edge[1] != protest_route[next_protest_index]:
                        self.dfs(edge[1], end, visited, path, protest_route, next_protest_index)
        
        # Si el destino de la tupla ya fue visitada, o hay una protesta, se elimina el origen del camino y de la 
        # lista de visitados                 
        path.pop()
        visited.remove(start)

    def generaArchivo(self, n, caminos, ruta, inicio, fin, soluciones):
        """"Método que genera el archivo"""        
        with open("solucion.txt", "w", encoding="utf-8") as archivo:
        
            archivo.write(n)
            for camino in caminos:
                archivo.write(camino[0] + " " + camino[1] + "\n")
                
            archivo.write(ruta + "\n") 
            archivo.write(inicio + " " + fin)
            for solucion in soluciones:
                archivo.write(solucion + "\n")   


 