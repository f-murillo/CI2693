import random
# Importar unittest y archivos a testear
import unittest
import Ejercicio1
import Ejercicio2
import Ejercicio3
import Ejercicio4

class test_Ejercicio1(unittest.TestCase):
    """Clase que realiza los tests para Ejercicio1.py"""
    
    def test_roy_warshall_v1_v2(self):
        """Función que hace el test que verifica si la 1ra versión del algoritmo de Roy-Warshall funciona correctamente
        Entrada: self: instancia de test_Ejercicio1, el cual es un testeador
        Salida: . si la prueba sale bien, o F si no funciona como debería
        
        Complejidad: O(n^3)
        """
        # Declarar matriz de prueba
        M_prueba = [[0,1,0,0],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
        # Declarar el resultado esperado de aplicar Roy-Warshall
        M_result = [[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]]
        # Aplicar Roy-Warhsall
        resultado = Ejercicio1.roy_warshall(M_prueba, len(M_prueba))
        # Aplicar una aserción que verifique si el resultado obtenido es igual al esperado
        self.assertEqual(resultado, M_result)  
        
    def test_roy_warshall_v2(self):
        """Función que hace el test que verifica si la 2da versión del algoritmo de Roy-Warshall funciona correctamente
        Entrada: self: instancia de test_Ejercicio1, el cual es un testeador
        Salida: . si la prueba sale bien, o F si no funciona como debería
        
        Complejidad: O(n^3)
        """
        # Declarar matriz de prueba
        M_prueba = [[0,1,0,0],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
        # Declarar el resultado esperado de aplicar Roy-Warshall (v2)
        M_result = [[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]]
        # Aplicar Roy-Warhsall (v2)
        resultado = Ejercicio1.roy_warshall_v2(M_prueba, len(M_prueba))
        # Aplicar una aserción que verifique si el resultado obtenido es igual al esperado
        self.assertEqual(resultado, M_result)    
        
class test_Ejercicio2(unittest.TestCase):
    """Clase que realiza el test para Ejercicio2.py"""
    
    def test_cc(self):
        """Función que hace el test que verifica si el algoritmo del cálculo de componentes conexas funciona correctamente
        Entrada: self: instancia de test_Ejercicio2, el cual es un testeador
        Salida: . si la prueba sale bien, o F si no funciona como debería
        
        Complejidad: O(n^3)
        """
        # Declarar matriz de prueba
        M_prueba = [[0,1,0,0],[1,0,1,0],[0,1,0,0],[0,0,0,0]]
        # Declarar el resultado esperado de aplicar el algoritmo que calcula las componentes conexas
        cc_result = [{0,1,2},{3}]
        # Aplicar el algoritmo
        resultado = Ejercicio2.componentes_conexas(M_prueba)
        # Aplicar una aserción que verifique si el resultado obtenido es igual al esperado
        self.assertEqual(resultado, cc_result)
        
class test_Ejercicio3(unittest.TestCase):
    """Clase que realiza el test para Ejercicio3.py"""
    
    def test_puntos_art(self):
        """Función que hace el test que verifica si el algoritmo del cálculo de puntos de articulación funciona correctamente
        Entrada: self: instancia de test_Ejercicio3, el cual es un testeador
        Salida: . si la prueba sale bien, o F si no funciona como debería
        
        Complejidad: O(n^4)
        """
        # Declarar matriz de prueba
        M_prueba = [[0,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0],[0,1,0,1,0,0,1,0],[0,0,1,0,1,1,0,0],
        [0,0,0,1,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,0,0,0,0,1,0]]
        # Declarar el resultado esperado de aplicar el algoritmo que calcula los puntos de articulación
        puntos_result = [1, 2, 3, 6]
        # Aplicar el algoritmo
        resultado = Ejercicio3.puntos_articulacion(M_prueba)
        # Aplicar una aserción que verifique si el resultado obtenido es igual al esperado
        self.assertEqual(resultado, puntos_result) 
        
class test_Ejercicio4(unittest.TestCase):
    """Clase que realiza el test para Ejercicio4.py (Revisar README.md para una descripción del ejemplo)"""
    def test_informe(self):
        """Función que hace el test para verificar si el algoritmo que genera el informe de la red social funciona
        correctamente
        
        Entrada: self: instancia de test_Ejercicio4, el cual es un testeador
        Salida: . si la prueba sale bien, o F si no funciona como debería
        
        Complejidad: O(n^4)
        """
        
        M_prueba = [[0,1,0,1,0,0,0,0,0],[1,0,1,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0],[1,0,1,0,1,0,0,0,0],
                 [0,0,0,1,0,1,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,0,0,1,0]]
        
        Ejercicio4.informe(M_prueba)
        # Leer el contenido del archivo generado
        with open("informe.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()
            
        contenido_esperado = [
            "Matriz que representa la red social:\n",
            "0 1 0 1 0 0 0 0 0\n",
            "1 0 1 0 0 0 0 0 0\n",
            "0 1 0 1 0 0 0 0 0\n",
            "1 0 1 0 1 0 0 0 0\n",
            "0 0 0 1 0 1 0 0 0\n",
            "0 0 0 0 1 0 0 0 0\n",
            "0 0 0 0 0 0 0 0 0\n",
            "0 0 0 0 0 0 0 0 1\n",
            "0 0 0 0 0 0 0 1 0\n",
            "---------------------------\n",
            "Matriz de alcance:\n",
            "1 1 1 1 1 1 0 0 0\n",
            "1 1 1 1 1 1 0 0 0\n",
            "1 1 1 1 1 1 0 0 0\n",
            "1 1 1 1 1 1 0 0 0\n",
            "1 1 1 1 1 1 0 0 0\n",
            "1 1 1 1 1 1 0 0 0\n",
            "0 0 0 0 0 0 1 0 0\n",
            "0 0 0 0 0 0 0 1 1\n",
            "0 0 0 0 0 0 0 1 1\n",
            "---------------------------\n",
            "Componentes conexas: [{0, 1, 2, 3, 4, 5}, {6}, {8, 7}]\n",
            "---------------------------\n",
            "Puntos de articulación: [3, 4]"
        ]
        
        # Aplicar una aserción que verifique si el resultado obtenido es igual al esperado
        self.assertEqual(contenido, contenido_esperado)    
        
if __name__ == '__main__':
    unittest.main()