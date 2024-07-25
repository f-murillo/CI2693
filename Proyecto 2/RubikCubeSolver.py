import copy
from collections import deque
from RubikCube import RubikCube


class RubikCubeSolver:
    def __init__(self, rubik_cube):
        self.rubik_cube = rubik_cube
        self.inverse_moves = {
            'rotate_left': 'rotate_right',
            'rotate_right': 'rotate_left',
            'rotate_up': 'rotate_down',
            'rotate_down': 'rotate_up',
            'rotate_front': 'rotate_back',
            'rotate_back': 'rotate_front'
        }

    def get_neighbors(self, cube):
        neighbors = []
        moves = [
            ('rotate_left', 'upper'),
            ('rotate_right', 'upper'),
            ('rotate_left', 'lower'),
            ('rotate_right', 'lower'),
            ('rotate_up', 'front'),
            ('rotate_down', 'front'),
            ('rotate_up', 'back'),
            ('rotate_down', 'back')
        ]

        for move, arg in moves:
            new_cube = self.copy_cube(cube)
            getattr(new_cube, move)(arg)
            neighbors.append((new_cube, move, arg))

        return neighbors

    def copy_cube(self, cube):
        new_cube = RubikCube()
        new_cube.upper.content = copy.deepcopy(cube.upper.content)
        new_cube.lower.content = copy.deepcopy(cube.lower.content)
        new_cube.upper.name = cube.upper.name
        new_cube.lower.name = cube.lower.name
        return new_cube

    def is_solved(self, cube):
        '''
        Función que verifica si el cubo está resuelto
        '''
        # Primero, debe cumplirse que en cada fila, el color del centro en los cuboides sea el mismo
        # Para la fila superior
        for cuboid in cube.upper.content:
            if cuboid.center != cube.upper.content[0].center:
                return False

        # Para la fila inferior
        for cuboid in cube.lower.content:
            if cuboid.center != cube.lower.content[0].center:
                return False

        # Luego, debe cumplirse que en cada fila que los lados adyacentes entre los cuboides sean iguales
        # Para la fila superior
        # Chequeamos los extremos
        if cube.upper.content[0].left != cube.upper.content[-1].right:
            return False
        for i in range(1, 3):
            if cube.upper.content[i - 1].right != cube.upper.content[i].left:
                return False
        # Para la fila inferior
        # Chequeamos los extremos
        if cube.lower.content[0].left != cube.lower.content[-1].right:
            return False
        for i in range(1, 3):
            if cube.lower.content[i - 1].right != cube.lower.content[i].left:
                return False

        # Finalmente, debe cumplirse que los colores de izquierda y derecha de las filas sean iguales entre sí
        for i in range(4):
            if cube.upper.content[i].left != cube.lower.content[i].left:
                return False
            if cube.upper.content[i].right != cube.lower.content[i].right:
                return False
        return True

    def solve(self):
        initial_state = self.rubik_cube
        if self.is_solved(initial_state):
            return []

        queue = deque([(initial_state, [])])
        visited = set()

        while queue:
            current_cube, path = queue.popleft()
            last_move = path[-1] if path else None

            cube_signature = self.cube_to_tuple(current_cube)

            if cube_signature in visited:
                continue

            visited.add(cube_signature)

            for neighbor, move, arg in self.get_neighbors(current_cube):
                if last_move is not None and arg == last_move[1] and self.inverse_moves[last_move[0]] == move:
                    continue  # Evita movimientos redundantes

                new_path = path + [(move, arg)]
                if self.is_solved(neighbor):
                    return new_path
                queue.append((neighbor, new_path))
        return None

    def cube_to_tuple(self, cube):
        '''
        Función que convierte la representación del cubo en una tupla
        '''

        upper = tuple([(cuboid.left, cuboid.center, cuboid.right)
                       for cuboid in cube.upper.content])
        lower = tuple([(cuboid.left, cuboid.center, cuboid.right)
                       for cuboid in cube.lower.content])
        cube_tuple = upper + lower

        return cube_tuple
