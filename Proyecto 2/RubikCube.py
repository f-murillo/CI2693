import numpy as np


class Cuboid():
    def __init__(self, number, left, center, right):
        '''
        Construimos un cuboide que contiene los colores de la cara izquierda, central (arriba o abajo) y derecha
        '''
        self.number = number
        self.left = left
        self.center = center
        self.right = right

    def to_string(self):
        '''
        Función que imprime los colores del cuboide
        '''
        print(f'Left: {self.left}, Center: {self.center}, Right: {self.right}')


class Row():
    '''
    Construimos una fila que contiene 4 cuboides
    '''

    def __init__(self, cuboid1, cuboid2, cuboid3, cuboid4, name):
        self.content = np.array([cuboid1, cuboid2, cuboid3, cuboid4])
        self.name = name

    def __str__(self):
        return self.name


class RubikCube():
    def __init__(self):
        self.upper = Row(
            Cuboid(0, 'B', 'Y', 'R'), Cuboid(1, 'R', 'Y', 'G'), Cuboid(
                2, 'G', 'Y', 'O'), Cuboid(3, 'O', 'Y', 'B'), 'upper'
        )
        self.lower = Row(
            Cuboid(4, 'B', 'W', 'R'), Cuboid(5, 'R', 'W', 'G'), Cuboid(
                6, 'G', 'W', 'O'), Cuboid(7, 'O', 'W', 'B'), 'lower'
        )

    def to_string(self):
        print('Upper')
        for cuboid in self.upper.content:
            print(cuboid.number, cuboid.left, cuboid.center, cuboid.right)
        print('Lower')
        for cuboid in self.lower.content:
            print(cuboid.number, cuboid.left, cuboid.center, cuboid.right)

    def rotate_left(self, row):
        '''
        Función que recibe la fila a rotar y rota los cuboides hacia la izquierda
        '''
        if row == 'upper':
            temp = self.upper.content[0]
            self.upper.content[0] = self.upper.content[1]
            self.upper.content[1] = self.upper.content[2]
            self.upper.content[2] = self.upper.content[3]
            self.upper.content[3] = temp

        if row == 'lower':
            temp = self.lower.content[0]
            self.lower.content[0] = self.lower.content[1]
            self.lower.content[1] = self.lower.content[2]
            self.lower.content[2] = self.lower.content[3]
            self.lower.content[3] = temp

    def rotate_right(self, row):
        '''
        Función que recibe la fila a rotar y rota los cuboides hacia la derecha
        '''
        if row == 'upper':
            temp = self.upper.content[3]
            self.upper.content[3] = self.upper.content[2]
            self.upper.content[2] = self.upper.content[1]
            self.upper.content[1] = self.upper.content[0]
            self.upper.content[0] = temp
        if row == 'lower':
            temp = self.lower.content[3]
            self.lower.content[3] = self.lower.content[2]
            self.lower.content[2] = self.lower.content[1]
            self.lower.content[1] = self.lower.content[0]
            self.lower.content[0] = temp

    def rotate_down(self, side):
        '''
        Función que recibe el lado a rotar (frente o atrás) hacia abajo
        '''
        if side == "front":
            # Creamos una matriz nueva con los elementos afectados
            temp_matrix = np.array([
                [self.upper.content[0],
                 self.upper.content[1]],
                [self.lower.content[0],
                 self.lower.content[1]],
            ])

            final_matrix = np.rot90(temp_matrix)
            # Ahora, actualizamos el estado del cubo
            self.upper.content[0] = final_matrix[0][0]
            self.upper.content[1] = final_matrix[0][1]
            self.lower.content[0] = final_matrix[1][0]
            self.lower.content[1] = final_matrix[1][1]

            # Ahora, debemos cambiar los colores de cada cuboide afectado
            # Para el cuboide en la primera posición de la fila superior
            temp = self.upper.content[0].center
            self.upper.content[0].center = self.upper.content[0].right
            self.upper.content[0].right = self.upper.content[0].left
            self.upper.content[0].left = temp

            # Para el cuboide en la segunda posición de la fila superior
            temp = self.upper.content[1].center
            self.upper.content[1].center = self.upper.content[1].right
            self.upper.content[1].right = temp

            # Para el cuboide en la primera posición de la fila inferior
            temp = self.lower.content[0].center
            self.lower.content[0].center = self.lower.content[0].left
            self.lower.content[0].left = temp

            # Para el cuboide en la primera posición de la fila superior
            temp = self.lower.content[1].right
            self.lower.content[1].right = self.lower.content[1].center
            self.lower.content[1].center = self.lower.content[1].left
            self.lower.content[1].left = temp

        elif side == "back":
            # Creamos una matriz nueva con los elementos afectados
            temp_matrix = np.array([
                [self.upper.content[2],
                 self.upper.content[3]],
                [self.lower.content[2],
                 self.lower.content[3]],
            ])

            final_matrix = np.rot90(temp_matrix, k=-1)
            # Ahora, actualizamos el estado del cubo
            self.upper.content[2] = final_matrix[0][0]
            self.upper.content[3] = final_matrix[0][1]
            self.lower.content[2] = final_matrix[1][0]
            self.lower.content[3] = final_matrix[1][1]

            # Ahora, debemos cambiar los colores de cada cuboide afectado
            # Para el cuboide en la tercera posición de la fila superior
            temp = self.upper.content[2].center
            self.upper.content[2].center = self.upper.content[2].left
            self.upper.content[2].left = temp

            # Para el cuboide en la cuarta posición de la fila superior
            temp = self.upper.content[3].right
            self.upper.content[3].right = self.upper.content[3].center
            self.upper.content[3].center = self.upper.content[3].left
            self.upper.content[3].left = temp

            # Para el cuboide en la tercera posición de la fila inferior
            temp = self.lower.content[2].left
            self.lower.content[2].left = self.lower.content[2].center
            self.lower.content[2].center = self.lower.content[2].right
            self.lower.content[2].right = temp

            # Para el cuboide en la cuarta posición de la fila inferior
            temp = self.lower.content[3].center
            self.lower.content[3].center = self.lower.content[3].right
            self.lower.content[3].right = temp

    def rotate_up(self, side):
        '''
        Función que recibe el lado a rotar (frente o atrás) hacia arriba
        '''
        if side == "front":
            # Creamos una matriz nueva con los elementos afectados
            temp_matrix = np.array([
                [self.upper.content[0],
                 self.upper.content[1]],
                [self.lower.content[0],
                 self.lower.content[1]],
            ])

            final_matrix = np.rot90(temp_matrix, k=-1)
            # Ahora, actualizamos el estado del cubo
            self.upper.content[0] = final_matrix[0][0]
            self.upper.content[1] = final_matrix[0][1]
            self.lower.content[0] = final_matrix[1][0]
            self.lower.content[1] = final_matrix[1][1]

            # Ahora, debemos cambiar los colores de cada cuboide afectado
            # Para el cuboide en la primera posición de la fila superior
            temp = self.upper.content[0].center
            self.upper.content[0].center = self.upper.content[0].left
            self.upper.content[0].left = temp

            # Para el cuboide en la segunda posición de la fila superior
            temp = self.upper.content[1].right
            self.upper.content[1].right = self.upper.content[1].center
            self.upper.content[1].center = self.upper.content[1].left
            self.upper.content[1].left = temp

            # Para el cuboide en la primera posición de la fila inferior
            temp = self.lower.content[0].left
            self.lower.content[0].left = self.lower.content[0].center
            self.lower.content[0].center = self.lower.content[0].right
            self.lower.content[0].right = temp

            # Para el cuboide en la primera posición de la fila superior
            temp = self.lower.content[1].center
            self.lower.content[1].center = self.lower.content[1].right
            self.lower.content[1].right = temp

        elif side == "back":
            # Creamos una matriz nueva con los elementos afectados
            temp_matrix = np.array([
                [self.upper.content[2],
                 self.upper.content[3]],
                [self.lower.content[2],
                 self.lower.content[3]],
            ])

            final_matrix = np.rot90(temp_matrix)
            # Ahora, actualizamos el estado del cubo
            self.upper.content[2] = final_matrix[0][0]
            self.upper.content[3] = final_matrix[0][1]
            self.lower.content[2] = final_matrix[1][0]
            self.lower.content[3] = final_matrix[1][1]

            # Ahora, debemos cambiar los colores de cada cuboide afectado
            # Para el cuboide en la tercera posición de la fila superior
            temp = self.upper.content[2].left
            self.upper.content[2].left = self.upper.content[2].center
            self.upper.content[2].center = self.upper.content[2].right
            self.upper.content[2].right = temp

            # Para el cuboide en la cuarta posición de la fila superior
            temp = self.upper.content[3].center
            self.upper.content[3].center = self.upper.content[3].right
            self.upper.content[3].right = temp

            # Para el cuboide en la tercera posición de la fila inferior
            temp = self.lower.content[2].center
            self.lower.content[2].center = self.lower.content[2].left
            self.lower.content[2].left = temp

            # Para el cuboide en la cuarta posición de la fila inferior
            temp = self.lower.content[3].right
            self.lower.content[3].right = self.lower.content[3].center
            self.lower.content[3].center = self.lower.content[3].left
            self.lower.content[3].left = temp

    def rotate_front(self, side):
        '''
        Función que recibe el lado a rotar (izquierda o derecha) hacia adelante
        '''
        if side == "right":
            # Creamos una matriz nueva con los elementos afectados
            temp_matrix = np.array([
                [self.upper.content[1],
                 self.upper.content[2]],
                [self.lower.content[1],
                 self.lower.content[2]],
            ])

            final_matrix = np.rot90(temp_matrix)
            # Ahora, actualizamos el estado del cubo
            self.upper.content[1] = final_matrix[0][0]
            self.upper.content[2] = final_matrix[0][1]
            self.lower.content[1] = final_matrix[1][0]
            self.lower.content[2] = final_matrix[1][1]

            # Ahora, debemos cambiar los colores de cada cuboide afectado
            # Para el cuboide en la segunda posición de la fila superior
            temp = self.upper.content[1].left
            self.upper.content[1].left = self.upper.content[1].center
            self.upper.content[1].center = self.upper.content[1].right
            self.upper.content[1].right = temp

            # Para el cuboide en la tercera posición de la fila superior
            temp = self.upper.content[2].center
            self.upper.content[2].center = self.upper.content[2].right
            self.upper.content[2].right = temp

            # Para el cuboide en la segunda posición de la fila inferior
            temp = self.lower.content[1].center
            self.lower.content[1].center = self.lower.content[1].left
            self.lower.content[1].left = temp

            # Para el cuboide en la tercera posición de la fila inferior
            temp = self.lower.content[2].right
            self.lower.content[2].right = self.lower.content[2].center
            self.lower.content[2].center = self.lower.content[2].left
            self.lower.content[2].left = temp

        elif side == "left":
            # Creamos una matriz nueva con los elementos afectados
            temp_matrix = np.array([
                [self.upper.content[0],
                 self.upper.content[3]],
                [self.lower.content[0],
                 self.lower.content[3]],
            ])

            final_matrix = np.rot90(temp_matrix)
            # Ahora, actualizamos el estado del cubo
            self.upper.content[0] = final_matrix[0][0]
            self.upper.content[3] = final_matrix[0][1]
            self.lower.content[0] = final_matrix[1][0]
            self.lower.content[3] = final_matrix[1][1]

            # Ahora, debemos cambiar los colores de cada cuboide afectado
            # Para el cuboide en la primera posición de la fila superior
            temp = self.upper.content[0].right
            self.upper.content[0].right = self.upper.content[0].center
            self.upper.content[0].center = self.upper.content[0].left
            self.upper.content[0].left = temp

            # Para el cuboide en la cuarta posición de la fila superior
            temp = self.upper.content[3].center
            self.upper.content[3].center = self.upper.content[3].left
            self.upper.content[3].left = temp

            # Para el cuboide en la primera posición de la fila inferior
            temp = self.lower.content[0].center
            self.lower.content[0].center = self.lower.content[0].right
            self.lower.content[0].right = temp

            # Para el cuboide en la cuarta posirightción de la fila inferior
            temp = self.lower.content[3].left
            self.lower.content[3].left = self.lower.content[3].center
            self.lower.content[3].center = self.lower.content[3].right
            self.lower.content[3].right = temp

    def rotate_back(self, side):
        '''
        Función que recibe el lado a rotar (izquierda o derecha) hacia atrás
        '''
        if side == "right":
            # Creamos una matriz nueva con los elementos afectados
            temp_matrix = np.array([
                [self.upper.content[1],
                 self.upper.content[2]],
                [self.lower.content[1],
                 self.lower.content[2]],
            ])

            final_matrix = np.rot90(temp_matrix, k=-1)
            # Ahora, actualizamos el estado del cubo
            self.upper.content[1] = final_matrix[0][0]
            self.upper.content[2] = final_matrix[0][1]
            self.lower.content[1] = final_matrix[1][0]
            self.lower.content[2] = final_matrix[1][1]

            # Ahora, debemos cambiar los colores de cada cuboide afectado
            # Para el cuboide en la segunda posición de la fila superior
            temp = self.upper.content[1].center
            self.upper.content[1].center = self.upper.content[1].left
            self.upper.content[1].left = temp

            # Para el cuboide en la tercera posición de la fila superior
            temp = self.upper.content[2].right
            self.upper.content[2].right = self.upper.content[2].center
            self.upper.content[2].center = self.upper.content[2].left
            self.upper.content[2].left = temp

            # Para el cuboide en la segunda posición de la fila inferior
            temp = self.lower.content[1].left
            self.lower.content[1].left = self.lower.content[1].center
            self.lower.content[1].center = self.lower.content[1].right
            self.lower.content[1].right = temp

            # Para el cuboide en la tercera posición de la fila inferior
            temp = self.lower.content[2].center
            self.lower.content[2].center = self.lower.content[2].right
            self.lower.content[2].right = temp

        elif side == "left":
            # Creamos una matriz nueva con los elementos afectados
            temp_matrix = np.array([
                [self.upper.content[0],
                 self.upper.content[3]],
                [self.lower.content[0],
                 self.lower.content[3]],
            ])

            final_matrix = np.rot90(temp_matrix, k=-1)
            # Ahora, actualizamos el estado del cubo
            self.upper.content[0] = final_matrix[0][0]
            self.upper.content[3] = final_matrix[0][1]
            self.lower.content[0] = final_matrix[1][0]
            self.lower.content[3] = final_matrix[1][1]

            # Ahora, debemos cambiar los colores de cada cuboide afectado
            # Para el cuboide en la primera posición de la fila superior
            temp = self.upper.content[0].center
            self.upper.content[0].center = self.upper.content[0].right
            self.upper.content[0].right = temp

            # Para el cuboide en la cuarta posición de la fila superior
            temp = self.upper.content[3].left
            self.upper.content[3].left = self.upper.content[3].center
            self.upper.content[3].center = self.upper.content[3].right
            self.upper.content[3].right = temp

            # Para el cuboide en la primera posición de la fila inferior
            temp = self.lower.content[0].right
            self.lower.content[0].right = self.lower.content[0].center
            self.lower.content[0].center = self.lower.content[0].left
            self.lower.content[0].left = temp

            # Para el cuboide en la cuarta posición de la fila inferior
            temp = self.lower.content[3].center
            self.lower.content[3].center = self.lower.content[3].left
            self.lower.content[3].left = temp
