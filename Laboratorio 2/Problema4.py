# Importar la clase deque (cola de doble extremo)
from collections import deque

def BFS_Laberinto(laberinto, inicio, fin, obstaculos_moviles):
    """Método que resuelve el problema del camino más corte en laberinto con obstáculos móviles usando BFS"""
    # Obtener las dimensiones del laberinto
    n = len(laberinto)
    m = len(laberinto[0])
    # Inicializar un conjunto para almacenar las celdas visitadas
    visitados = set()
    # Inicializar una cola con la celda de inicio y un camino vacío
    cola = deque([((inicio, []), 0)])  
    # Definir los posibles movimientos (derecha, abajo, izquierda, arriba)
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]  

    # Mientras la cola no esté vacía
    while cola:
        # Sacar la celda y el tiempo actuales de la cola
        ((x, y), camino), tiempo = cola.popleft()
        # Agregar la celda actual al camino
        camino.append((x, y))  
        # Si la celda actual es el final, devolvemos el camino
        if (x, y) == fin:
            return camino  
        # Para cada posible movimiento
        for dx, dy in movimientos:
            # Calcular las coordenadas de la celda siguiente
            nx, ny = x + dx, y + dy
            siguiente = (nx, ny)
            # Si la celda siguiente está dentro del laberinto, no es una pared y no ha sido visitada
            if 0 <= nx < n and 0 <= ny < m and laberinto[nx][ny] == 0 and (siguiente, tiempo + 1) not in visitados:
                # Asumimos que es seguro moverse a la celda siguiente
                es_seguro = True
                # Para cada obstáculo móvil
                for obstaculo in obstaculos_moviles:
                    # Obtener la ruta del obstáculo y su posición actual y siguiente
                    ruta = obstaculo['ruta']
                    # Calcular la posición actual del obstáculo
                    # Nota: el operador % asegura que el obstáculo se mueva de manera indefinida 
                    # en la ruta dada
                    actual_obstaculo = ruta[tiempo % len(ruta)]
                    # Calcular la posición del obstáculo una unidad de tiempo después
                    siguiente_obstaculo = ruta[(tiempo + 1) % len(ruta)]
                    # Si la celda siguiente es la posición actual o siguiente del obstáculo
                    if siguiente == actual_obstaculo or siguiente == siguiente_obstaculo:
                        # No es seguro moverse a la celda siguiente, por lo que se sale del ciclo
                        es_seguro = False
                        break
                # Si es seguro moverse a la celda siguiente
                if es_seguro:
                    # Agregar la celda siguiente y su camino a la cola
                    cola.append(((siguiente, camino[:]), tiempo + 1))  
                    # Marcar la celda siguiente como visitada
                    visitados.add((siguiente, tiempo + 1))
    # Si no se encuentra un camino, se devuelve None
    return None

def main():
    laberinto = [
        [0 , 0 , 0 , 0 , 0] ,
        [0 , 1 , 0 , 1 , 0] ,
        [0 , 1 , 0 , 1 , 0] ,
        [0 , 0 , 0 , 1 , 0] ,
        [0 , 0 , 0 , 0 , 0]
    ]
    # Inicio y fin 1
    inicio1 = (0 , 0)
    fin1 = (4 , 4)
    # Obstáculos móviles 1
    obstaculos_moviles1 = [
        {'ruta': [(1 , 1) , (2 , 1) , (3 , 1) ] , 'actual': (1 ,1) }
    ]
    
    print(BFS_Laberinto(laberinto, inicio1, fin1, obstaculos_moviles1))
    
if __name__ == "__main__":
    main()    