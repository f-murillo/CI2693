# Rubik Cube Solver

Integrantes:

- Franco Murillo 16-10782
- Eliezer Cario 18-10605
- Fredthery Castro 18-10783

## Descripción General

Este proyecto implementa un solucionador para un cubo de Rubik simplificado utilizando Python. El cubo de Rubik se representa en un estado bidimensional con filas superiores e inferiores, y se proporcionan funciones para generar estados aleatorios y resolver el cubo. 

### Estructura de Archivos

- `RubikCube.py`: Define la representación del cubo de Rubik y las operaciones que se pueden realizar sobre él.
- `RandomRubikCube.py`: Implementa un generador de estados aleatorios del cubo.
- `RubikCubeSolver.py`: Implementa el solucionador del cubo de Rubik utilizando búsqueda en anchura (BFS).

## Representación del Estado

El cubo de Rubik se representa utilizando clases que modelan sus componentes:

### Clases Principales

- **Cuboid**: Representa un cuboide individual con tres colores (izquierda, centro, el cual puede ser arriba o abajo, y derecha).
- **Row**: Representa una fila de 4 cuboides.
- **RubikCube**: Representa el cubo de Rubik completo, con una fila superior de tipo `Row`(`upper`) y una fila inferior de tipo `Row` (`lower`).

### Estado del Cubo

El estado del cubo se define por los colores de los cuboides en las filas superior e inferior. Por ejemplo, un cuboide en la fila superior podría tener los colores 'B' (izquierda), 'Y' (centro) y 'R' (derecha).

## Transiciones

Las transiciones representan movimientos que se pueden realizar en el cubo. Cada transición modifica el estado del cubo y se puede describir como una rotación de los cuboides en una fila o un lado del cubo. También, al momento de ejecutar algún movimiento se toman en cuenta los cambios en las posiciones de los colores de cada cuboide, para rotar correctamente toda la estructura del cubo.

### Movimientos Disponibles

- **Rotaciones Horizontales**:
  - `rotate_left`: Rota los cuboides de una fila hacia la izquierda.
  - `rotate_right`: Rota los cuboides de una fila hacia la derecha.

- **Rotaciones Verticales**:
  - `rotate_up`: Rota los cuboides de un lado (frontal o trasero) hacia arriba.
  - `rotate_down`: Rota los cuboides de un lado (frontal o trasero) hacia abajo.

- **Rotaciones en Profundidad**:
  - `rotate_front`: Rota los cuboides de un lado (izquierdo o derecho) hacia el frente.
  - `rotate_back`: Rota los cuboides de un lado (izquierdo o derecho) hacia atrás.

## Funcionamiento del Solucionador

El solucionador utiliza una búsqueda en anchura (BFS) para encontrar la secuencia de movimientos que resuelve el cubo. 

### Proceso de Solución

1. **Inicialización**: El solucionador comienza con el estado inicial del cubo.
2. **Generación de Vecinos**: Para cada estado, genera sus estados vecinos aplicando todos los movimientos posibles.
3. **Verificación de Solución**: Verifica si alguno de los estados vecinos es una solución.
4. **Evitación de Ciclos**: Utiliza un conjunto de estados visitados para evitar ciclos y movimientos redundantes.
5. **Evitar redundancia de movimientos**: Verifica, a través de un conjunto de movimientos y sus inversos que no se repitan movimientos en la solución, es decir, que no se haga un movimiento inicial e inmediatamente después de éste un inverso, pues esto significaría que se volvió al estado inicial.
6. **Camino Solucionador**: Si encuentra una solución, devuelve la secuencia de movimientos necesarios para resolver el cubo.

Para la verificación de la solución en la función `is_solved()`, se utilizan los siguientes criterios del patrón que debe tener el cubo para considerarse "resuelto:
1. Primero, debe cumplirse que en cada fila, el color del centro en los cuboides sea el mismo. Es decir, la cara superior o inferior (dependiendo de la fila en la que estemos) debe ser la misma para todos los cuboides.
2. Luego, debe cumplirse que en cada fila que los lados adyacentes entre los cuboides sean iguales. Así, por ejemplo, si tenemos los cuboides [A, B, C ,D] sabemos que el color de la derecha de A debe ser igual al colore de la izquierda de B. También se toman a consideración los extremos, donde el color izquierdo de A debe ser igual al color derecho de D.
3. Finalmente, debe cumplirse que los colores de izquierda y derecha de las filas sean iguales entre sí. Es decir, que si tenemos [A,B,C,D] como fila superior y [E,F,G,H] como fila inferior, para cada elemento en la misma posición, sus dos colores deben ser iguales (esto es, en un caso particular, que los colores a la izquierda y derecha de A sean iguales a los colores a la izquierda y derecha de E).

### Funciones Principales del Solucionador

- `get_neighbors(cube)`: Genera todos los estados vecinos aplicando cada movimiento posible.
- `copy_cube(cube)`: Crea una copia profunda del cubo para evitar modificar el estado original.
- `is_solved(cube)`: Verifica si el estado actual del cubo es una solución.
- `solve()`: Ejecuta el algoritmo BFS para encontrar la secuencia de movimientos que resuelve el cubo.
- `cube_to_tuple(cube)`: Convierte el estado del cubo en una tupla para facilitar su almacenamiento en el conjunto de estados visitados.

## Sobre el tiempo de ejecución
La cantidad máxima de movimientos aleatorios únicos que fuimos capaz de procesar dentro de un tiempo "razonable" y un uso de memoria (sin ser tan excesivo) fueron 9, esto se debe probablemente a la cantidad de opciones que se generan a partir de un movimiento y los subsecuentes al mismo (es decir, los vecinos generados en cada iteración del solucionador). Sin embargo, creemos que este enfoque utilizado en el proyecto nos permite observar un poco mejor el comportamiento del cubo, además de ser claro y conciso en código, permitiendo adaptarlo a futuras mejoras o implementaciones externas.

## Paquetes adicionales
Se debe instalar el paquete `numpy` para la correcta ejecución del código.

## Ejemplo de Uso

```python
from RandomRubikCube import RandomRubikCube
from RubikCubeSolver import RubikCubeSolver

# Crear una instancia del cubo de Rubik
rubik_cube = RandomRubikCube().generate_random_cube()

# Crear una instancia del solucionador
solver = RubikCubeSolver(rubik_cube)

# Resolver el cubo
solution = solver.solve()

# Imprimir la solución
if solution is not None:
  print("La secuencia de movimientos para resolver el cubo es:")
  for sol in solution:
    print(f"{sol[0]} {sol[1]}")
else:
    print("No se encontró solución.")
