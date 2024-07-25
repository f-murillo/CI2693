import unittest
import orden

class test_orden(unittest.TestCase):
    """Clase que se encarga del test del algoritmo de orden topológico
    NOTA: Revisar archivos ejemplo.txt, ejemplo2.txt y ejemplo3.txt para evitar confusiones al momento de revisar 
    las soluciones"""
    def test_orden_topologico(self):
        """Test del orden topologico"""
        # Prueba 1
        archivo1 = 'ejemplo1.txt'
        # Capas y número de trimestres que faltan esperados
        capas_e1 = [{'', 'Matemática III'},
                            {'Estructuras Discretas I', 'Lógica Simbólica', 'Matemática IV'},
                            {'Laboratorio de Algoritmos y Estructuras I', 'Estructuras Discretas II', 'Algoritmos y Estructuras I', 'Matemática V'},
                            {'Estructuras Discretas III', 'Probabilidad para Ingenieros', 'Algoritmos y Estructuras II', 'Laboratorio de Algoritmos y Estructuras II', 'Cálculo Numérico'},
                            {'Organización del Computador', 'Estadística', 'Modelos Lineales', 'Laboratorio de Algoritmos y Estructuras III', 'Algoritmos y Estructuras III'},
                            {'Laboratorio de Lenguajes de Programación', 'Sistemas de Operación I', 'Sistemas de Bases de Datos I', 'Traductores e Interpretadores', 'Laboratorio de Bases de Datos I', 'Lenguajes de Programación', 'Interfaces con el Usuario'},
                            {'Ingeniería del Software I', 'Redes de Computadoras', 'Sistemas de Información I'},
                            {'Electiva de Área I'},
                            {'Electiva de Área II'},
                            {'Electiva de Área III'},
                            {'Electiva de Área IV'},
                            {'Electiva de Área V'},
                            {'Electiva de Área VI'}]
        
        n_t_e1 = 13
        # Obtener resultados usando el algoritmo
        capas_o1 = orden.solution(archivo1)
        n_t_o1 = len(capas_o1)
        # Comparar resultados
        self.assertEqual(capas_e1, capas_o1)
        self.assertEqual(n_t_e1, n_t_o1)
        
        # Prueba 2
        archivo2 = 'ejemplo2.txt'
        # Capas y número de trimestres que faltan esperados
        capas_e2 = [{'', 'Mate I'},
                    {'Mate II', 'Fisica I'},
                    {'Fisica II'}]
        n_t_e2 = 3
        # Obtener resultados usando el algoritmo
        capas_o2 = orden.solution(archivo2)
        n_t_o2 = len(capas_o2)
        # Comparar resultados
        self.assertEqual(capas_e2, capas_o2)
        self.assertEqual(n_t_e2, n_t_o2)
        
        # Prueba 3
        archivo3 = 'ejemplo3.txt'
        # Capas y número de trimestres que faltan esperados
        capas_e3 = [{'Matemática II', ''},
                    {'Lógica Simbólica', 'Matemática III', 'Física I'},
                    {'Laboratorio de Algoritmos y Estructuras I', 'Estructuras Discretas I', 'Matemática IV', 'Física II', 'Algoritmos y Estructuras I'},
                    {'Cálculo Numérico', 'Algoritmos y Estructuras II', 'Estructuras Discretas II', 'Laboratorio de Algoritmos y Estructuras II', 'Matemática V'},
                    {'Organización del Computador', 'Estructuras Discretas III', 'Algoritmos y Estructuras III'},
                    {'Lenguajes de Programación', 'Sistemas de Bases de Datos I'},
                    {'Sistemas de Información I'}]
        n_t_e3 = 7
        # Obtener resultados usando el algoritmo
        capas_o3 = orden.solution(archivo3)
        n_t_o3 = len(capas_o3)
        # Comparar resultados
        self.assertEqual(capas_e3, capas_o3)
        self.assertEqual(n_t_e3, n_t_o3)
    
    
if __name__ == '__main__':
    unittest.main()  