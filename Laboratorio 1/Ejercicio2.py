# Importar desde el archivo Ejercicio1.py la función que calcula la matriz de alcance usando la 2da versión del algoritmo
# de Roy-Warshall
from Ejercicio1 import roy_warshall_v2

def componentes_conexas(M):
    """Función que calcula las componentes conexas de un grafo representado con una matriz de adyacencias
    
    Entrada: M: matriz de adyacencias
    Salida: CC: lista de conjuntos de componentes conexas
    
    Complejidad: O(n^3)
    """
    # Calcular la matriz de alcanzabilidad M_star usando el algoritmo de Roy-Warshall que importamos
    n = len(M)
    M_star = roy_warshall_v2(M, n)
    # Inicializar el conjunto de vértices restantes y el conjunto de componentes conexas
    Resto = set(range(n))
    CC = []
    
    # Iterar hasta que no queden vértices en Resto
    while Resto:
        # Seleccionar un elemento aleatorio de Resto
        v = Resto.pop()
        # Inicializar la componente conexa actual
        comp = {v}
        # Encontrar todos los vértices alcanzables desde v y agregarlos a la componente conexa
        for w in range(n):
            if M_star[v][w] and M_star[w][v]:
                comp.add(w)
        # Agregar la componente conexa al conjunto de componentes conexas y actualizar Resto
        CC.append(comp)
        Resto -= comp
    return CC
