import unittest
import Prim
import Kruskal

class test_Prim(unittest.TestCase):
    """Clase que se encarga del test del algoritmo de Prim"""
    def test_AMC_Prim(self):
        """Test de Prim"""
        # Prueba 1
        conjuntos_residenciales1 = [(2, 3), (5, 7), (8, 10), (1,2), (3,4)]
        central1 = (4,9)
        # Resultados esperados
        amc1_e = [((2, 3), (1, 2)), ((2, 3), (3, 4)), ((3, 4), (5, 7)), ((5, 7), (4, 9)), ((4, 9), (8, 10))]
        costo_total1_e = 12.79315200332763
        # Obtener resultado aplicando algoritmo de Prim
        amc1, costo_total1 = Prim.prim(conjuntos_residenciales1,central1)
        # Comparar resultados
        self.assertEqual(amc1_e, amc1)
        self.assertEqual(costo_total1_e, costo_total1)
        
        # Prueba 2
        conjuntos_residenciales2 = [(1, 2), (3, 4), (5, 6), (7,8), (9,10), (15,3)]
        central2 = (2,8)
        amc2_e = [((1, 2), (3, 4)), ((3, 4), (5, 6)), ((5, 6), (7, 8)), ((7, 8), (9, 10)), ((5, 6), (2, 8)), ((9, 10), (15, 3))]
        costo_total2_e = 24.138804231741638
        
        amc2, costo_total2 = Prim.prim(conjuntos_residenciales2,central2)
        # Comparar resultados
        self.assertEqual(amc2_e, amc2)
        self.assertEqual(costo_total2_e, costo_total2)
        
class test_Kruskal(unittest.TestCase):
    def test_AMC_Kruskal(self):
        # Prueba 1
        conjuntos_residenciales1 = [(2, 3), (5, 7), (8, 10), (1,2), (3,4)]
        central1 = (4,9)
        # Resultados esperados
        amc1_e = [((2, 3), (1, 2)), ((2, 3), (3, 4)), ((5, 7), (4, 9)), ((5, 7), (3, 4)), ((8, 10), (4, 9))]
        costo_total1_e = 12.79315200332763
        # Obtener resultado aplicando algoritmo de Kruskal
        amc1, costo_total1 = Kruskal.kruskal(conjuntos_residenciales1,central1)
        # Comparar resultados
        self.assertEqual(amc1_e, amc1)
        self.assertEqual(costo_total1_e, costo_total1)
        
        # Prueba 2
        conjuntos_residenciales2 = [(1, 2), (3, 4), (5, 6), (7,8), (9,10), (15,3)]
        central2 = (2,8)
        # Resultados esperados
        amc2_e = [((1, 2), (3, 4)), ((3, 4), (5, 6)), ((5, 6), (7, 8)), ((7, 8), (9, 10)), ((5, 6), (2, 8)), ((9, 10), (15, 3))]
        costo_total2_e = 24.138804231741638
        # Obtener resultado aplicando algoritmo de Kruskal
        amc2, costo_total2 = Kruskal.kruskal(conjuntos_residenciales2,central2)
        # Comparar resultados
        self.assertEqual(amc2_e, amc2)
        self.assertEqual(costo_total2_e, costo_total2)        
        
if __name__ == '__main__':
    unittest.main()        
        
        
        
       
    
