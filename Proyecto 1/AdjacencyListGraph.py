import copy
class AdjacencyListGraph:
    """Clase que implementa un grafo dirigido usando una Lista de Adyacencias"""
    
    def __init__(self):
        """Método constructor"""
        # Inicializa un diccionario vacío para representar el grafo
        self.grafo = {}
        
    def size(self):
        """Método que retorna el número de vértices del grafo"""
        # Retorna el número de claves en el diccionario del grafo, que representa el número de vértices
        return len(self.grafo)

    def contains_vertex(self, vertice):
        """Metodo que verifica si un vértice está o no en el grafo"""
        # Retorna True si el grafo tiene al menos un vértice y el vértice dado está en el grafo
        return self.size() > 0 and vertice in self.grafo
    
    def contains_adyacent(self, origen, destino):
        """Método que verifica si el vértice destino está en la lista de adyacentes del vértice origen"""
        # Retorna True si el vértice destino está en la lista de vértices adyacentes del vértice origen
        return destino in self.grafo[origen]
    
    def add_vertex(self, vertice):
        """Método que agrega un vértice al grafo"""
        # Si el vértice no está en el grafo
        if not self.contains_vertex(vertice):
            # Agrega el vértice al grafo con una lista vacía de vértices adyacentes
            self.grafo[vertice] = []
            # Retorna True para indicar que el vértice fue agregado exitosamente
            return True
        # Si el vértice ya estaba en el grafo, retorna False
        return False

    def add_edge(self, origen, destino):
        """Método que agrega un arco al grafo"""
        # Si el grafo está vacío
        if self.size() == 0:
            return False
        # Verificar si ambos vértices pertenecen al grafo
        if self.contains_vertex(origen) and self.contains_vertex(destino):
            # Si el arco no existe en el grafo, se agrega
            if not self.contains_adyacent(origen, destino):
                self.grafo[origen].append(destino)
                return True
            return False
        return False
    
    def remove_vertex(self, vertice):
        """Método que elimina un vértice del grafo"""
        # Si el grafo está vacío
        if self.size() == 0:
            return False
        # Si el vértice pertenece al grafo
        if self.contains_vertex(vertice):
            # Eliminar vértice
            del self.grafo[vertice]
            # Buscar listas donde aparezca el vértice y eliminarlo
            for key in list(self.grafo.keys()):
                if vertice in self.grafo[key]:
                    self.grafo[key].remove(vertice)
            return True
        return False

    def  remove_edge(self, origen, destino):
        """Método que elimina un arco del grafo"""
        # Si el grafo está vacío
        if self.size() == 0:
            return False
        # Si ambos vértices pertenecen al grafo
        if self.contains_vertex(origen) and self.contains_vertex(destino):
            # Si el arco pertenece al grafo, se elimina
            if self.contains_adyacent(origen, destino):
                self.grafo[origen].remove(destino)
                return True
            return False
        return False

    def  get_inward_edges(self, vertice):
        """Método que retorna una lista de los predecesores de un vértice"""
        # Si el grafo está vacío o el vértice no pertenece al grafo
        if self.size() == 0 or not self.contains_vertex(vertice):
            return False
        # Declarar lista con los predecesores
        aristas_inbound = []
        # Buscar aquellos elementos para el cual el vértice esté en la lista de adyacentes, y se agrega la clave a la lista de predecesores
        for key, value in self.grafo.items():
            if vertice in value:
                aristas_inbound.append(key)
        return aristas_inbound

    def get_outward_edges(self, vertice):
        """Método que retorna una lista de los sucesores de un vértice"""
        # Si el grafo está vacío o el vértice no está en el grafo
        if self.size() == 0 or not self.contains_vertex(vertice):
            return False
        # Retornar lista de adyecentes de la clave
        return self.grafo.get(vertice, [])

    def get_vertices_connected_to(self, vertice):
        """Método que retorna una lista con los ayacentes de un vértice, tanto si el vértice es el de origen, como si es el de destino"""
        # Si el grafo está vacío o el vértice no está en el grafo
        if self.size() == 0 or not self.contains_vertex(vertice):
            return False
        # Declarar lista con los adyacentes del vértice
        vertices_conectados = []
        # Buscar en el grafo todas las incidencias del vértice, tanto si es de origen, como si es de destino, y se agregan los vértices con los que incide 
        # el vértice dado
        for key, value in self.grafo.items():
            if vertice in value:
                vertices_conectados.append(key)
            if key == vertice:
                vertices_conectados.append(value)    
        return vertices_conectados

    def get_all_vertices(self):
        """Método que retorna una lista con los vértices del grafo"""
        # Retorna una lista con las claves 
        return list(self.grafo.keys())

    def subgraph(self, vertices):
        """Método que retorna un subgrafo del grafo"""
        # Si el grafo está vacío
        if self.size() == 0:
            return False
        # Declarar el subgrafo
        subgrafo = AdjacencyListGraph()
        # Para cada vértice en la colección de vértices
        for vertice in vertices:
            # Si el vértice efectivamente existe en el grafo orifinal, se agrega al subgrafo
            if self.contains_vertex(vertice):
                subgrafo.add_vertex(vertice)
                for v in self.get_outward_edges(vertice):
                    # Nos aseguramos de que el vértice al que apunta el arco también está en la colección de vértices, y luego se agrega el
                    # arco al subgrafo
                    if v in vertices:  
                        subgrafo.add_edge(vertice, v) 
        return subgrafo


    def complement(self):
        """Método que retorna el grafo complemento de un grafo"""
        # Si el grafo está vacío
        if self.size() == 0:
            return False        
        # Declarar el grafo complemento
        grafo_complemento = AdjacencyListGraph()
        # Recorremos todos los vértices del grafo
        for vertice in self.get_all_vertices():
            # Agregar vértice al grafo complemento
            grafo_complemento.add_vertex(vertice)
            # Para todos los demás vértices
            for otro_vertice in self.get_all_vertices():
                # Si son distintos, y otro_vertice no es un sucesor del vértice, se agrega el arco hasta él
                if otro_vertice != vertice and (otro_vertice not in self.get_outward_edges(vertice)):
                    grafo_complemento.add_edge(vertice, otro_vertice)
        return grafo_complemento

    def copy(self):
        """Método que retorna una copia del grafo"""
        return copy.deepcopy(self) 