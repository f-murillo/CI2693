def find_infinite_money(casas_de_cambio, moneda_inicial=None):
    """Método que verifica si se puede obtener ganancias infinitamente"""
    n = len(casas_de_cambio) # Numero de casas de cambio
    # Si no se especifica la moneda inicial, asumimos la moneda local
    if moneda_inicial is None:
        moneda_inicial = "MonedaLocal"

    # Inicializar las valores con la moneda inicial
    valores = {moneda_inicial: 1.0}

    # Construir el diccionario de tasas de cambio
    tasas_de_cambio = {}
    for casa in casas_de_cambio:
        for moneda, (buy, sell) in casa.items():
            tasas_de_cambio[moneda] = sell / buy
            
    updated = True # Indicador de que si se cambió algún valor
    i = 0 # Iterador
    # Actualizar valores
    while i < n and updated:
        updated = False
        for casa in casas_de_cambio:
            for moneda, (buy, sell) in casa.items():
                if moneda == moneda_inicial:
                    continue
                new_value = valores[moneda_inicial] * sell
                if new_value > valores.get(moneda, 0.0):
                    valores[moneda] = new_value
                    updated = True
        i += 1

    # Verificar si alguna moneda puede aumentar infinitamente su valor
    for moneda, valor in valores.items(): 
        if valor > 1.0:
            return True

    return False

# Ejemplo 
casas_de_cambio = [
    {"Moneda1": (1, 2), "Moneda2": (1, 1)},
    {"Moneda1": (0.55, 1), "Moneda2": (3, 4)}
]

resultado = find_infinite_money(casas_de_cambio, moneda_inicial="Moneda1")
print(resultado)  # True