import random
from RubikCube import RubikCube


class RandomRubikCubeGenerator:
    """Clase que implementa el generador de instancias aleatorias del cubo Rubik"""

    def __init__(self, num_moves=9):
        self.num_moves = num_moves  # Número de movimientos aleatorios para mezclar el cubo

    def generate_random_cube(self):
        """Método que crea la instancia del cubo Rubik con un estado aleatorio válido"""
        cube = RubikCube()  # Crear un cubo Rubik en estado resuelto
        moves_fb = [cube.rotate_up, cube.rotate_down]
        moves_lr = [cube.rotate_front, cube.rotate_back]
        moves_basic = [cube.rotate_left, cube.rotate_right]

        last_move = (None, None)

        # Aplicar una serie de movimientos aleatorios al cubo
        for _ in range(self.num_moves):
            choice = random.choice([0, 1, 2])
            if choice == 0:
                move = random.choice(moves_fb)
                argum = random.choice(["front", "back"])

            elif choice == 1:
                move = random.choice(moves_lr)
                argum = random.choice(["left", "right"])
            else:
                move = random.choice(moves_basic)
                argum = random.choice(["upper", "lower"])

            # ejecutamos el movimiento
            move(argum)

        return cube
