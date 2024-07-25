def DFS_N_Reinas(n):
    """Método que resuelve el problema de las N reinas usando DFS recursivo"""
    # Inicializar una lista vacía para almacenar todas las soluciones posibles
    soluciones = []
    # Llamar a la función recursiva para colocar las reinas en el tablero
    DFS_Recursivo(n, 0, [], soluciones)
    # Devolver las soluciones encontradas
    return soluciones

def DFS_Recursivo(n, fila, posicion, soluciones):
    """Método que consigue las soluciones de manera recursiva"""
    # Si todas las reinas están colocadas de manera segura, agregar la solución a la lista de soluciones
    if fila == n:
        soluciones.append(posicion[:])
        return
    # Intentar colocar una reina en cada columna de la fila actual
    for col in range(n):
        # Verificar si es seguro colocar una reina en la fila y columna actuales
        if es_Seguro(posicion, fila, col):
            # Si es seguro, colocar una reina en la posición actual y avanzar a la siguiente fila
            posicion.append((fila, col))
            DFS_Recursivo(n, fila + 1, posicion, soluciones)
            # Si no se puede colocar una reina en la siguiente fila, se retrocede y se quita la reina de la posición actual
            posicion.pop()

def es_Seguro(posicion, fila_ocupada, col_ocupada):
    """Método que verifica si es seguro colocar una reina en la fila y columna dadas"""
    # Verificar si hay una reina en la misma columna o en las diagonales
    for i in range(fila_ocupada):
        if posicion[i][1] == col_ocupada or \
            posicion[i][0] - posicion[i][1] == fila_ocupada - col_ocupada or \
            posicion[i][0] + posicion[i][1] == fila_ocupada + col_ocupada:
            # Si hay una reina en la misma columna o en las diagonales, no es seguro colocar una reina aquí
            return False
    # Si no hay una reina en la misma columna ni en las diagonales, es seguro colocar una reina aquí
    return True