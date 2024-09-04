import math

def time_adjusted(distance, initial_v, slope):
    """Calcula el tiempo de viaje ajustado teniendo en cuenta la pendiente de la carretera.

    Args:
        distance (float): La distancia a recorrer.
        initial_v (float): La velocidad inicial.
        slope (float): La pendiente de la carretera en grados.

    Returns:
        float: El tiempo de viaje ajustado.

    Raises:
        ValueError: Si la pendiente es de 90 grados o -90 grados.

    """
    # Transformar la pendiente de grados a radianes
    if slope == 90 or slope == -90:
        raise ValueError("The slope cannot be 90 degrees.")
    pen = (slope * math.pi) / 180

    # Calcula la velocidad ajustada (tomando en cuenta la pendiente)
    adjusted_velocity = initial_v * math.cos(pen)

    # Calcula el tiempo de viaje ajustado
    return distance / adjusted_velocity

def bellman_gas_consumption(road_network, road_network_free, start_city, end_city, initial_velocity, gasoline_consumption_per_km, initial_gasoline, max_time_extension_factor):
    """Método que implementa el algoritmo de Bellman para calcular el consumo de gasolina de la ruta óptima entre dos ciudades
    y el tiempo que toma realizar el viaje

    Args:
        road_network (dict): Un diccionario que representa la red de carreteras, donde las claves son las ciudades y los valores son listas de tuplas que representan las ciudades vecinas, sus distancias y pendientes.
        road_network_free (list): Una lista de ciudades donde el repostaje de gasolina es gratuito.
        start_city (str): La ciudad de inicio.
        end_city (str): La ciudad de destino.
        initial_velocity (float): La velocidad inicial del vehículo.
        gasoline_consumption_per_km (float): El consumo de gasolina por kilómetro.
        initial_gasoline (float): La cantidad inicial de gasolina en el vehículo.
        max_time_extension_factor (float): El factor máximo de extensión del tiempo.

    Retorna:
        tuple: Una tupla que contiene el consumo óptimo de gasolina y el tiempo de viaje para la ruta entre la ciudad de inicio y la ciudad de destino. Si no hay una ruta posible, devuelve (None, None).
    """
    # Inicialización
    cities = list(road_network.keys())  # Lista de ciudades
    n = len(cities) # Número de ciudades
    inf = float('inf') # Costo inicial de las ciudades 
    cost = {city: inf for city in cities}  # Diccionario de costos
    cost[start_city] = 0 # Costo de la ciudad inicial
    time = 0 # Acumulador del tiempo de viaje de la ciudad inicial a la final
    
    # Iterar n-1 veces
    for _ in range(n-1):
        # Para cada ciudad de la lista de ciudades
        for city in cities:
            # Para cada ciudad, con su distancia y su pendiente de la ruta de ciudades
            for w, distance, slope in road_network[city]:
                # Calcular tiempo de viaje ideal
                travel_time = distance / initial_velocity
                # Calcular tiempo ajustado a la pendiente
                travel_time_adjusted = time_adjusted(distance, initial_velocity, slope)
                # Calcular consumo de gasolina entre ciudades
                gas_consumption = (distance * gasoline_consumption_per_km) * ( 1 + (slope / 100) )
                # Si la ciudad está en la lista de ciudades con recarga de gasolina gratis
                if city in road_network_free:
                    gas_consumption *= -1
                # Si el consumo de gasolina es menor a la gasolina que se tiene, y el tiempo ajustado es menor o igual al tiempo ideal con el factor de extension maximo
                if (gas_consumption < initial_gasoline) and (travel_time_adjusted <= travel_time * max_time_extension_factor):
                    # Si el costo de u + el consumo de gasolina de ir de u a w es menor al costo de w
                    if cost[city] + gas_consumption < cost[w]:
                        time += travel_time_adjusted # Agregar tiempo de viaje al acumulador
                        cost[w] = cost[city] + gas_consumption # Actualizar costo de w
                        initial_gasoline -= gas_consumption # Restar el consumo de gasolina a la gasolina que se tiene 
    
    # Verificar si hay algún ciclo de costo negativo, consiguiendo el consumo de gasolina igual que antes
    for city in cities:
        for w, distance, slope in road_network[city]:
            gas_consumption = (distance * gasoline_consumption_per_km) * ( 1 + (slope / 100) )
            if city in road_network_free:
                gas_consumption *= -1
            # Si el costo de u + el consumo de gasolina de ir de u a w es menor al costo de w: Error, ciclo negativo
            if cost[city] + gas_consumption < cost[w] and cost[w] != inf:
                raise ValueError("El grafo contiene un ciclo de costo negativo.")
        
    # Si el costo final es infinito, no hay ruta posible
    if cost[end_city] == inf:
        return None, None
    return cost[end_city], time
