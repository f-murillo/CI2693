# Importar desde el archivo Ejercicio2.py la función que calcula las componentes conexas
from Ejercicio2 import componentes_conexas

def eliminarVertice(M,v):
    """Función que elimina un vértice de un grafo representado como una matriz de adyacencias
    
    Entrada: M: matriz de adyacencias
    Entrada: v: vértice a eliminar
    Salida: M_nuevo: matriz de adyacencias resultante de eliminar el vértice 
    
    Complejidad: O(n^2)
    """
    n = len(M)
    # Declarar una nueva matriz de tamaño n-1
    M_nuevo = [[0] * (n-1) for _ in range(n-1)]
    
    # Declarar el primer indice que se usará para agregar elementos a la nueva matriz 
    k = 0
    # Iterar sobre los elementos de la matriz
    for i in range(n):
        # Si el indice i es distinto al vértice a eliminar
        if i != v:
            # Declarar el segundo indice que se usará para agregar elementos a la nueva matriz 
            l = 0
            for j in range(n):
                # Si el indice j es distinto al vértice a eliminar
                if j != v:
                    # Agregar a la nueva matriz en la posición [k][l] el elemento de la matriz original en la posición [i][j]
                    M_nuevo[k][l] = M[i][j]
                    # Incrementar índice l
                    l += 1
            # Incrementar índice k        
            k += 1        
                    
    return M_nuevo                

def puntos_articulacion(M):
    """Función que calcula los puntos de articulación de un grafo
    
    Entrada: M: matriz de adyacencias
    Salida: puntos_art: lista de puntos de articulación
    
    Complejidad: O(n^4)
    """
    
    n = len(M)
    # Declarar la lista que contendrá los puntos de articulación
    puntos_art = []
    # Calcular las componentes conexas de la matriz original, y tomar su longitud
    num_cc_original = len(componentes_conexas(M))
    
    # Iterar sobre todos los vértices 
    for i in range(n):
        # Eliminar el vértice i de la matriz original
        M_nueva = eliminarVertice(M,i)
        # Calcular las componentes conexas de la nueva matriz, y tomar su longitud
        num_cc_nueva = len(componentes_conexas(M_nueva))
        # Si el n° de comp. conexas de la nueva matriz es mayor al de la original, agregar i a la lista
        if(num_cc_nueva > num_cc_original):
            puntos_art.append(i)
            
    return puntos_art
 