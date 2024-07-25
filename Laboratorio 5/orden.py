from collections import defaultdict 

def leer_entrada(archivo):
    """Método que se encarga de leer el archivo"""
    with open(archivo, 'r', encoding="utf-8") as f:
        lineas = f.readlines()
    
    requisitos = defaultdict(list)
    correquisitos = []
    materias_actuales = []
    
    seccion = None
    for linea in lineas:
        linea = linea.strip()
        if linea.startswith("#"):
            seccion = linea
        elif seccion == "# Requisitos":
            if ":" in linea:
                materia, reqs = linea.split(":")
                requisitos[materia.strip()] = [r.strip() for r in reqs.split(",") if r.strip()]
        elif seccion == "# Correquisitos":
            correquisitos.append(tuple(linea.split(",")))
        elif seccion == "# Trimestre":
            materias_actuales = [materia.strip() for materia in linea.split(",")]
    
    return requisitos, correquisitos, materias_actuales

def construir_grafo(requisitos, correquisitos):
    """Método que construye el grafo dados los requisitos y correquisitos"""
    grafo = defaultdict(set) # El grafo se representara con un diccionario
    
    # Para cada materia y requisitos del diccionario de requisitos
    for materia, reqs in requisitos.items():
        # Para cada requisito de la lista de requisitos
        for req in reqs:
            # Agregar requisito de la materia
            grafo[materia].add(req)
    
    for linea in correquisitos:
        # Si la longitud de la linea es 2, hay correquisitos, por lo que se agregan al grafo
        if len(linea) == 2:
            c1, c2 = linea
            # Cada materia de la tupla sera requisito de la otra
            grafo[c1.strip()].add(c2.strip())
            grafo[c2.strip()].add(c1.strip())
    # Retornar grafo
    return grafo

def partition_by_levels(precedence_graph):
    """Método que se encarga de hacer el particionamiento por capas del grafo"""
    levels = [] # Lista de Niveles
    # Mientras el grafo no este vacio
    while precedence_graph: 
        level = set() # Conjunto que contendra los elementos de cada nivel
        # Para cada materia con sus requisitos en el grafo
        for node, requirements in list(precedence_graph.items()):
            # Si la materia no tiene requisitos, o si es correquisito y solo queda esa materia como requisito, se agrega al nivel
            if not requirements or all(req in precedence_graph and node in precedence_graph[req] and len(precedence_graph[req]) == 1 for req in requirements):
                level.add(node)
        # Si no hay elementos en el nivel despues del ciclo for, se termina el ciclo while        
        if not level:
            break
        # Agregar al nivel a la lista de niveles
        levels.append(level)
        # Para cada nodo del nivel
        for node_level in level:
            # Para cada lista de requisitos del grafo
            for requirements in precedence_graph.values():
                # Eliminar el nodo del nivel de la lista de requisitos
                requirements.discard(node_level)
            # Eliminar del grafo el nodo del nivel    
            del precedence_graph[node_level]
    # Retornar lista de niveles        
    return levels

def solution(archivo):
    """Método que acopla los métodos anteriores para resolver el problema"""
    # Obtener los requisitos, correquisitos y las materias actuales del archivo
    requisitos, correquisitos, materias_actuales = leer_entrada(archivo)
    materias_cursadas = set(materias_actuales)
    
    # Añadir todas las materias que son requisitos de las materias actuales
    for materia in materias_actuales:
        if materia in requisitos:
            materias_cursadas.update(requisitos[materia])
    
    # Construir grafo
    grafo = construir_grafo(requisitos, correquisitos)
    
    # Eliminar las materias cursadas del grafo
    for materia in materias_cursadas:
        if materia in grafo:
            del grafo[materia]
    for materia in grafo:
        grafo[materia] -= materias_cursadas
    
    # Obtener capas
    capas = partition_by_levels(grafo)
    
    # Añadir las materias actuales a la primera capa
    if materias_actuales:
        capas.insert(0, set(materias_actuales))
        
    return capas  
  
