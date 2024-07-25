def roy_warshall(M, n):
    """Algoritmo de Roy Warshall para calcular la matriz de alcance (v1)
    
    Entrada: M: Matriz de adyacencias
    Entrada: n: número de vértices del Grafo
    Salida: M_star: Matriz de alcance
    
    Complejidad Temporal: O(n^3)
    """
    # Inicializar la matriz de alcanzabilidad con ceros
    M_star = [[0] * n for _ in range(n)]
    
     # Inicializar M_star con las distancias iniciales de M, y con la Matriz Identidad
    for i in range(n):
        for j in range(n):
            M_star[i][j] = 1 if M[i][j] or i == j else 0
            
    # Aplicar el algoritmo de Roy-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                M_star[i][j] = M_star[i][j] or (
                M_star[i][k] and M_star[k][j])
    return M_star

def roy_warshall_v2(M, n):
    """Algoritmo de Roy Warshall para calcular la matriz de alcance (v2)
    
    Entrada: M: Matriz de adyacencias
    Entrada: n: número de vértices del Grafo
    Salida: M_star: Matriz de alcance
    
    Complejidad Temporal: O(n^3)
    """
    
    # Inicializar la matriz de alcanzabilidad con ceros
    M_star = [[0] * n for _ in range(n)]
    
    # Inicializar M_star con las distancias iniciales de M, y con la Matriz Identidad
    for i in range(n):
        for j in range(n):
            # Hay una arista directa de i a j
            M_star[i][j] = 1 if M[i][j] or i == j else 0
            
    # Aplicar el algoritmo de Roy-Warshall v2
    for k in range(n):
        for i in range(n):
            # Verificar si k es alcanzable desde i
            if M_star[i][k] == 1 and i != k: 
                for j in range(n):
                    # Si i es alcanzable desde j o j es alcanzable desde k, cualquiera de los dos valores es 1, 
                    # en caso contrario ambos valores son 0. Guardar el máximo valor
                    M_star[i][j] = max(M_star[i][j], M_star[k][j])
    return M_star

  