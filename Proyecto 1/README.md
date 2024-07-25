# Integrantes
- Franco Murillo 16-10782
- Eliezer Cario 18-10605
- Fredthery Castro 18-10783

# Proyecto 1: Implementación de un grafo dirigido con lista de adyacencias usando diccionario y listas

- Sea el grafo dirigido G = (V, E) el grafo a implementar
- Se implementa con un diccionario, cuyas claves son los vértices del grafo, y los valores son las listas de adyacencias correspondientes a cada vértice

Métodos de la clase

- __init__: Método constructor 
    - Inicializa el diccionario vacío
    - Complejidad: O(1)

- size: Método que retorna el número de vértices del grafo
    - Retorna la longitud del diccionario
    - Complejidad: O(1)

- contains_vertex: Método que verifica si un vértice pertenece al grafo
    - Verifica si el grafo no está vacío, y luego realiza la búsqueda del vértice en el diccionario
    - Complejidad: O(1)

- contains_adyacent: Método que verifica si un vértice destino pertenece a la lista de adyacencias de otro vértice origen
    - Busca el vértice origen en el diccionario
    - Busca el vértice destino en la lista de adyacentes del vértice origen
    - Complejidad: O(|V|)

- add_vertex: Método que agrega un vértice al grafo
    - Verifica si el vértice no estaba ya en el grafo
    - Agrega el vértice al diccionario con una lista vacía de adyacentes
    - Complejidad: O(1) 

- add_edge: Método que agrega un arco al grafo, dados un vértice de origen y un vértice destino
    - Verifica que el grafo no está vacío
    - Verifica que ambos vértices pertenezcan al grafo
    - Verifica que el vértice destino no esté en la lista de adyacencias del vértice de origen
    - Agrega a la lista de adyacencias del vértice origen al vértice destino
    - Complejidad: O(|V|)

- remove_vertex: Método que elimina un vértice del grafo
    - Verifica si el grafo no está vacío
    - Verifica si el vértice pertenece al grafo
    - Elimina el vértice del diccionario
    - Busca todas las listas de adyacencias donde está el vértice, y lo elimina de ésta
    - Complejidad: O((|V|)^2), ya que luego de eliminar el vértice del diccionario, recorre todos los otros vértices, y para cada uno, recorre su lista de adyacentes

- remove_edge: Método que elimina un arco del grafo, dados un vértice de origen y un vértice destino 
    - Verifica si el grafo no está vacío
    - Verifica que ambos vértices pertenezcan al grafo
    - Verifica que el vértice destino esté en la lista de adyacencias del vértice de origen
    - Elimina el vértice destino de la lista de adyacencias del vértice de origen
    - Complejidad: O(|V|)

- get_inward_edges: Método que retorna los predecesores de un vértice dado
    - Verifica si el grafo no está vacío o si el vértice no existe en el grafo
    - Declara la lista de predecesores
    - Busca en el diccionario todos aquellas claves que tenga en su lista de adyacentes el vértice dado
    - Guarda en la lista las claves
    - Complejidad: O((|V|)^2), ya que debe buscar para cada otro vértice del grafo, si el vértice dado aparece en su lista de adyacentes

- get_outward_edges: Método que retorna los sucesores de un vértice dado
    - Verifica si el grafo no está vacío o si el vértice no existe en el grafo
    - Busca el vértice en el diccionario y retorna su lista de adyacencias
    - Complejidad: O(1)

- get_vertices_connected_to: Método que retorna una lista con los vértices adyacentes a un vértice dado, ya sea si este vértice es de origen o de destino
    - Verifica si el grafo no está vacío o si el vértice no existe en el grafo
    - Declara una lista con los adyacentes del vértice
    - Busca las incidencias del vértice en el diccionario
    - Agrega los vértices que inciden con el vértice dado
    - Complejidad: O((|V|)^2)

- get_all_vertices: Método que retorna una lista con todos los vértices del grafo
    - Retorna una lista con las claves del diccionario
    - Complejidad: O(|V|)

- subgraph: Método que retorna un subgrafo dado una coleccioón de vértices V´ que es subconjunto de V
    - Verifica si el grafo no está vacío
    - Declara el subgrafo
    - Se verifica si cada vértice de la colección pertenece al grafo original, y se agrega al subgrafo
    - Se verifica si los sucesores de cada vértice de la colección está en la colección, y se agrega a su lista de adyacentes
    - Complejidad: O((|V|)^2) 

- complement: Método que retorna el grafo complemento de un grafo
    - Verifica si el grafo no está vacío
    - Declara el complemento
    - Agrega todos los vértices del grafo original al complemento
    - Para cada vértice v (por ejemplo), verifica si para cualquier otro vértice u, u está o no en la lista de adyacencias de v. Si no está, lo agrega
    - Complejidad: O((|V|)^3)

- copy: Retorna una copia del grafo
    - Usa la clase copy y retorna el método deepcopy
    - Complejidad: O(|V| + |E|)           
