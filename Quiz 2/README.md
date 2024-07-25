# Quiz 2 - Franco Murillo - 1610782

# El problema
Dada una lista de casas de cambio, y una moneda inicial, se quiere determinar si se puede realizar cambios de manera que se pueda obtener dinero infinito

# Estrategia
• Sea el grafo G = (V,E), donde:
    • V son las monedas (llamaremos a |V| n)
    • E son las tasas de cambio (llamaremos a |E| m)
• Se utilizó un enfoque greedy para resolver el problema, ya que permite tomar decisiones óptimas locales para cada paso, en el que se considera la tasa de cambio disponible en cada casa de cambio. 

• El algoritmo comparte similitud con el Algoritmo de Bellman en cuanto a estructura, mas no en funcionamiento

# Algoritmo
• Se inicializa las variables a usar (número de casas de cambio (n), valores de las monedas, diccionario de tasas de cambio)
• Se inicializa el indicador de cambio (update) en True, y un iterador i en cero
• Mientras i sea menor a n, y además update sea True:
    • Cambiamos update a falso
    • Se sigue un esquema parecido a Bellman para la actualización de costos, pero al revés, si se encuentra un costo mayor, se actualiza 
• Al salir del ciclo principal, se itera a través de las monedas:
    • Si algún valor de moneda es mayor a 1.0, se puede aumentar su valor infinitamente, por lo que se retorna True
• Si se logra salir del ciclo, no hay moneda a la que se pueda aumentar su valor infinitamente, por lo que se retorna false    

# Complejidad temporal
• Construir el diccionario de tasas de cambio tiene complejidad O(m)
• El ciclo principal para actualizar los valores tiene complejidad O(n)
    • Dentro del ciclo principal, se itera a través de todas las tasas de cambio y sus monedas. Esto tiene complejidad O(n * m)
• El ciclo que verifica si alguna moneda puede incrementar infinitamente tiene complejidad O(n)
• Finalmente, la complejidad total es O(n * m)
