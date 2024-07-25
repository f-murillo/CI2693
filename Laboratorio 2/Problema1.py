def DFS_Laberinto(laberinto, inicio, fin):
    """Método para resolver el problema del laberinto usando DFS recursivo"""
    # Declarar conjunto para almacenar las celdas que ya hemos visitado
    visitados = set()  
    # Declarar lista para almacenar el camino desde el inicio hasta el fin
    camino = []  
    # Si se encuentra un camino hasta el fin, devolver el camino
    if DFS_Recursivo(laberinto, inicio, fin, visitados, camino):
        return camino
    # Si no se encuentra, se develve None
    return None

def DFS_Recursivo(laberinto, actual, fin, visitados, camino):
    """Método que aplica el DFS recursivo"""
    x, y = actual  # Coordenadas de la celda actual
    # Si la celda actual está fuera del laberinto, es una pared, o ya ha sido visitada, retornar False
    if x < 0 or y < 0 or x >= len(laberinto) or y >= len(laberinto[0]) or laberinto[x][y] == 1 or actual in visitados:
        return False
    camino.append(actual)  # Agregamos la celda actual al camino
    # Si la celda actual es el fin, hemos encontrado un camino, por lo que retornamos True
    if actual == fin:
        return True
    visitados.add(actual)  # Se marca la celda actual como visitada
    # Para cada vecino de la celda actual, se intenta encontrar un camino hasta el final
    for vecino in obtener_vecinos(laberinto, actual):
        if DFS_Recursivo(laberinto, vecino, fin, visitados, camino):
            return True
    # Si no se encuentra un camino desde la celda actual hasta la final, se elimina la celda actual del camino
    camino.pop()
    return False

def obtener_vecinos(laberinto, posicion):
    """Método que obtiene los vecinos válidos de una celda"""
    x, y = posicion  # Coordenadas de la celda actual
    # Se define los vecinos como las celdas arriba, abajo, a la izquierda y a la derecha de la celda actual
    # Esto generará el siguiente orden de exploración del DFS: abajo, derecha, izquierda, arriba
    vecinos = [(x+1, y), (x, y+1), (x, y-1), (x-1, y)]  
    vecinos_validos = []  # Lista para almacenar los vecinos válidos
    # Para cada vecino (nx,ny) (nuevo x, nuevo y), si está dentro del laberinto y no es una pared, se considera válido, y se agrega
    for nx, ny in vecinos:
        if nx >= 0 and ny >= 0 and nx < len(laberinto) and ny < len(laberinto[0]):
            if laberinto[nx][ny] == 0:
                vecinos_validos.append((nx, ny))
    # Devolver la lista de vecinos válidos
    return vecinos_validos