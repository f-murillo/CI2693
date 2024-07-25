# Importar funciones de Ejercicio1.py, Ejercicio2.py y Ejercicio3.py
from Ejercicio1 import roy_warshall_v2
from Ejercicio2 import componentes_conexas
from Ejercicio3 import puntos_articulacion

def informe(M):
    """Función que genera un informe de una red social simulada, representada por un grafo implementado con una 
    matriz de adyacencias
    
    Entrada: M: matriz de adyacencias
    Salida: "informe.txt": archivo de texto con el informe
    
    Complejidad: O(n^4)
    """
    n = len(M)
    # Calculos
    
    # Matriz de adyacencias
    M_a = roy_warshall_v2(M,n)
    
    # Componentes Conexas
    cc = componentes_conexas(M)
    
    # Puntos de Articulación
    puntos_art = puntos_articulacion(M)
    
    # Declaramos un separador para el informe
    separador = "---------------------------"
    
    # Generar informe en archivo llamado informe.txt
    with open("informe.txt", "w", encoding="utf-8") as archivo:
        
        # Imprimir Matriz original
        archivo.write("Matriz que representa la red social:\n")
        for fila in M:
            linea = ' '.join(map(str, fila))
            archivo.write(linea + "\n")
        
        # Imprimir separación 
        archivo.write(separador + "\n")
        
        # Imprimir la matriz de alcance
        archivo.write("Matriz de alcance:\n")
        for fila in M_a:
            linea = ' '.join(map(str, fila))
            archivo.write(linea + "\n")
        
        # Imprimir separación    
        archivo.write(separador + "\n")
        
        # Imprimir componentes conexas
        archivo.write(f"Componentes conexas: {cc}\n")
        
        # Imprimir separación
        archivo.write(separador + "\n")
        
        # Imprimir puntos de articulación
        archivo.write(f"Puntos de articulación: {puntos_art}")
             