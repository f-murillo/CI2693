# Importar unittest y archivos a testear
import unittest
import Problema1
import Problema2
import Problema3
import Problema4

class test_Problema1(unittest.TestCase):
    """Clase que realiza el test del problema 1"""
    def test_Laberinto_DFS(self):
        """Método que testea el funcionamiento del algoritmo DFS que resuelve el problema del laberinto"""
        # Laberinto de prueba 1
        laberinto1 = [
            [0, 1, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0]
        ]

        # Definir los puntos inicial y final
        inicio1 = (0, 0)
        fin1 = (7, 7)
        
        # Camino esperado
        camino_e1 = [
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), 
            (5, 0), (6, 0), (7, 0), (7, 1), (7, 2), 
            (6, 2), (6, 3), (6, 4), (7, 4), (7, 5), 
            (6, 5), (6, 6), (6, 7), (7, 7)
        ]
        
        # Obtener el camino con el algoritmo
        camino_o1 = Problema1.DFS_Laberinto(laberinto1, inicio1, fin1)
        # Comparar resultados
        self.assertEqual(camino_e1, camino_o1)
        
        ##################################################################
        # Laberinto de prueba 2
        laberinto2 = [
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 0]
        ]
        
        # Definir los puntos inicial y final
        inicio2 = (1,0)
        fin2 = (4,5)
        
        # Camino esperado
        camino_e2 = [
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
            (6, 0), (7, 0), (8, 0), (8, 1), (8, 2), 
            (7, 2), (7, 1), (6, 1), (6, 2), (5, 2),
            (5, 1), (4, 1), (3, 1), (2, 1), (2, 2),
            (2, 3), (3, 3), (4, 3), (4, 4), (5, 4),
            (5, 5), (5, 6), (4, 6), (4, 5)
        ]
        
        # Obtener el camino con el algoritmo
        camino_o2 = Problema1.DFS_Laberinto(laberinto2, inicio2, fin2)
        # Comparar resultados
        self.assertEqual(camino_e2, camino_o2)
        
class test_Problema2(unittest.TestCase):
    """Clase que realiza el test del problema 2"""
    def test_Camino_BFS(self):
        """Método que testea el funcionamiento del algoritmo que encuentra el camino más corto entre dos vértices usando BFS"""
        
        # Grafo de prueba 1
        grafo1 = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F','G'],
            'F': ['C', 'E'],
            'G': ['E','A']
        } 
        # Inicio y fin 1
        inicio1 = 'A'
        fin1 = 'G'
        # Camino esperado
        camino_e1 = ['A', 'B', 'E', 'G']
        # Obtener camino usando el algoritmo
        camino_o1 = Problema2.BFS(grafo1, inicio1, fin1)
        # Comparar los resultados
        self.assertEqual(camino_e1, camino_o1)
        
        ###################################################   
        # Grafo de prueba 2
        grafo2 = {
            1: [3, 7],
            2: [4, 1, 5],
            3: [6],
            4: [5, 7],
            5: [2, 4],
            6: [1, 4],
            7: []
        } 
        # Inicio y fin 1
        inicio2 = 5
        fin2 = 7
        # Camino esperado
        camino_e2 = [5, 4, 7]
        # Obtener camino usando el algoritmo
        camino_o2 = Problema2.BFS(grafo2, inicio2, fin2)
        # Comparar los resultados
        self.assertEqual(camino_e2, camino_o2) 
        
class test_Problema3(unittest.TestCase):
    """Clase que realiza del test del problema 3"""
    def test_N_Reinas(self):
        """Método que testea el funcionamiento del algoritmo que resuelve el problema de las N-Reinas usando DFS"""
        # Prueba 1
        # N1
        n1 = 4
        # Soluciones esperadas
        soluciones_e1 = [[(0, 1), (1, 3), (2, 0), (3, 2)], [(0, 2), (1, 0), (2, 3), (3, 1)]]
        # Obtener soluciones usando el algoritmo
        soluciones_o1 = Problema3.DFS_N_Reinas(n1)
        # Comparar resultados
        self.assertEqual(soluciones_e1, soluciones_o1)
        
        ####################################################
        # Prueba 2
        # N2
        n2 = 6
        # Soluciones esperadas
        soluciones_e2 = [
            [(0, 1), (1, 3), (2, 5), (3, 0), (4, 2), (5, 4)], 
            [(0, 2), (1, 5), (2, 1), (3, 4), (4, 0), (5, 3)], 
            [(0, 3), (1, 0), (2, 4), (3, 1), (4, 5), (5, 2)],
            [(0, 4), (1, 2), (2, 0), (3, 5), (4, 3), (5, 1)]
        ]
        # Obtener soluciones usando el algoritmo 
        soluciones_o2 = Problema3.DFS_N_Reinas(n2)
        # Comparar resultados
        self.assertEqual(soluciones_e2, soluciones_o2)
               
class test_Problema4(unittest.TestCase):
    """Método que realiza el test del problema 4"""
    def test_Lab_OM(self):
        """Método que testea el funcionamiento del algoritmo que encuentra el camino más corto en un laberinto usando BFS"""
        # Prueba 1
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
        # Camino esperado
        camino_e1 = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
        # Obtener camino usando el algoritmo
        camino_o1 = Problema4.BFS_Laberinto(laberinto, inicio1, fin1, obstaculos_moviles1)
        # Comparar resultados
        self.assertEqual(camino_e1, camino_o1)
        
        #################################################
        # Prueba 2
        laberinto2 = [
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 0, 1, 0]
        ]
        # Inicio y fin 2
        inicio2 = (1 , 0)
        fin2 = (4 , 5)
        # Obstáculos móviles 2
        obstaculos_moviles2 = [
            {'ruta': [(4 , 2) , (4 , 3) , (4 , 4), (4, 5), (4, 6), (4, 7)] , 'actual': (4 , 2) }
        ]   
        # Camino esperado
        camino_e2 = [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
        # Obtener camino usando el algoritmo
        camino_o2 = Problema4.BFS_Laberinto(laberinto2, inicio2, fin2, obstaculos_moviles2)
        # Comparar resultados
        self.assertEqual(camino_e2, camino_o2)
        
if __name__ == '__main__':
    unittest.main()