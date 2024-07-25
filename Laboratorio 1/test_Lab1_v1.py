# Importar archivos a testear
import Ejercicio1
import Ejercicio2
import Ejercicio3
import Ejercicio4
   
def test_roy_warshall():
    """Función que hace el test que verifica si la 1ra versión del algoritmo de Roy-Warshall funciona correctamente
    Entrada: self: instancia de test_Ejercicio1, el cual es un testeador
    Salida: . si la prueba sale bien, o F si no funciona como debería
        
    Complejidad: O(n^3)
    """
    print("Prueba: Roy-Warshall\n")
    # Declarar matriz de prueba
    M_prueba = [[0,1,0,0],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
    print("Matriz de prueba:\n" + 
            "0 1 0 0\n" +
            "0 0 1 1\n" + 
            "0 0 0 1\n" + 
            "0 0 0 0")
    # Declarar el resultado esperado de aplicar Roy-Warshall
    print("\nMatriz de alcance esperada:\n" + 
            "1 1 1 1\n" + 
            "0 1 1 1\n" + 
            "0 0 1 1\n" + 
            "0 0 0 1")
    # Aplicar Roy-Warhsall
    resultado = Ejercicio1.roy_warshall(M_prueba, len(M_prueba))
    print("\nMatriz de alcance obtenida por Roy-Warshall:")
    for i in range(len(resultado)):
        for j in range(len(resultado)):
            print(resultado[i][j], end=' ')
        print()
    
    print("\n---------------------------")
                
def test_roy_warshall_v2():
    """Función que hace el test que verifica si la 2da versión del algoritmo de Roy-Warshall funciona correctamente
    Entrada: self: instancia de test_Ejercicio1, el cual es un testeador
    Salida: . si la prueba sale bien, o F si no funciona como debería
        
    Complejidad: O(n^3)
    """
    print("\nPrueba: Roy-Warshall (V2)\n")
    # Declarar matriz de prueba
    M_prueba = [[0,1,0,0],[0,0,1,1],[0,0,0,1],[0,0,0,0]]
    print("Matriz de prueba:\n" + 
          "0 1 0 0\n" +
          "0 0 1 1\n" + 
          "0 0 0 1\n" + 
          "0 0 0 0")
    # Declarar el resultado esperado de aplicar Roy-Warshall
    print("\nMatriz de alcance esperada:\n" + 
          "1 1 1 1\n" + 
          "0 1 1 1\n" + 
          "0 0 1 1\n" + 
          "0 0 0 1")
    # Aplicar Roy-Warhsall (v2)
    resultado = Ejercicio1.roy_warshall_v2(M_prueba, len(M_prueba))
    print("\nMatriz de alcance obtenida por Roy-Warshall (V2):")
    for i in range(len(resultado)):
        for j in range(len(resultado)):
            print(resultado[i][j], end=' ')
        print()
        
    print("\n---------------------------")
        
   
def test_cc():
    """Función que hace el test que verifica si el algoritmo del cálculo de componentes conexas funciona correctamente
    Entrada: self: instancia de test_Ejercicio2, el cual es un testeador
    Salida: . si la prueba sale bien, o F si no funciona como debería
        
    Complejidad: O(n^3)
    """
    print("\nPrueba: Cálculo de componentes conexas\n")
    # Declarar matriz de prueba
    M_prueba = [[0,1,0,0],[1,0,1,0],[0,1,0,0],[0,0,0,0]]
    print("Matriz de prueba:\n" + 
          "0 1 0 0\n" +
          "1 0 1 0\n" +
          "0 1 0 0\n" +
          "0 0 0 0\n")
    # Aplicar el algoritmo
    resultado = Ejercicio2.componentes_conexas(M_prueba)
    # Imprimir resultados esperados y obtenidos
    print("Componentes conexas esperadas: [{0, 1,2 }, {3}]")
    print(f"Componentes conexas obtenidas: {resultado}\n")
    
    print("\n---------------------------")
        

def test_puntos_art():
    """Función que hace el test que verifica si el algoritmo del cálculo de puntos de articulación funciona correctamente
    Entrada: self: instancia de test_Ejercicio3, el cual es un testeador
    Salida: . si la prueba sale bien, o F si no funciona como debería
        
    Complejidad: O(n^4)
    """
    print("\nPrueba: Cálculo de puntos de articulación\n")
    # Declarar matriz de prueba
    M_prueba = [[0,1,0,0,0,0,0,0],[1,0,1,0,0,0,0,0],[0,1,0,1,0,0,1,0],[0,0,1,0,1,1,0,0],
    [0,0,0,1,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,0,0,0,0,1,0]]
    print("Matriz de prueba:\n" + 
          "0 1 0 0 0 0 0 0\n" + 
          "1 0 1 0 0 0 0 0\n" +
          "0 1 0 1 0 0 1 0\n" +
          "0 0 1 0 1 1 0 0\n" +
          "0 0 0 1 0 1 0 0\n" +
          "0 0 0 1 1 0 0 0\n" +
          "0 0 0 1 0 0 0 1\n" +
          "0 0 0 0 0 0 1 0\n")
    # Aplicar el algoritmo
    resultado = Ejercicio3.puntos_articulacion(M_prueba)
    # Imprimir resultados esperados y obtenidos      
    print("Puntos de articulación esperados: [1, 2, 3, 6]")
    print(f"Puntos de articulación obtenidos: {resultado}\n")
    
    print("\n---------------------------")
        
def test_informe():
    """Función que hace el test para verificar si el algoritmo que genera el informe de la red social funciona
    correctamente
        
    Entrada: self: instancia de test_Ejercicio4, el cual es un testeador
    Salida: . si la prueba sale bien, o F si no funciona como debería
        
    Complejidad: O(n^4)
    """
    print("\nPrueba: Informe\n")    
    M_prueba = [[0,1,0,1,0,0,0,0,0],[1,0,1,0,0,0,0,0,0],[0,1,0,1,0,0,0,0,0],[1,0,1,0,1,0,0,0,0],
                [0,0,0,1,0,1,0,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1],
                [0,0,0,0,0,0,0,1,0]]
        
    Ejercicio4.informe(M_prueba)
    # Leer el contenido del archivo generado
    with open("informe.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.readlines()
            
    print("Archivo esperado:\n" + 
        "\nMatriz que representa la red social:\n" +
        "\n0 1 0 1 0 0 0 0 0\n" +
        "\n1 0 1 0 0 0 0 0 0\n" +
        "\n0 1 0 1 0 0 0 0 0\n" +
        "\n1 0 1 0 1 0 0 0 0\n" +
        "\n0 0 0 1 0 1 0 0 0\n" +
        "\n0 0 0 0 1 0 0 0 0\n" +
        "\n0 0 0 0 0 0 0 0 0\n" +
        "\n0 0 0 0 0 0 0 0 1\n" +
        "\n0 0 0 0 0 0 0 1 0\n" +
        "\n---------------------------\n" +
        "\nMatriz de alcance:\n" + 
        "\n1 1 1 1 1 1 0 0 0\n" +
        "\n1 1 1 1 1 1 0 0 0\n" +
        "\n1 1 1 1 1 1 0 0 0\n" +
        "\n1 1 1 1 1 1 0 0 0\n" +
        "\n1 1 1 1 1 1 0 0 0\n" +
        "\n1 1 1 1 1 1 0 0 0\n" +
        "\n0 0 0 0 0 0 1 0 0\n" +
        "\n0 0 0 0 0 0 1 0 0\n" +
        "\n0 0 0 0 0 0 0 1 1\n" +
        "\n0 0 0 0 0 0 0 1 1\n" +
        "\n---------------------------\n" +
        "\nComponentes conexas: [{0, 1, 2, 3, 4, 5}, {6}, {8, 7}]\n" +
        "\n---------------------------\n" +
        "\nPuntos de articulación: [3, 4]\n"
    )
        
    print("Archivo obtenido:\n")
    for linea in contenido:
        print(linea)

def main():
    test_roy_warshall()
    test_roy_warshall_v2()
    test_cc()
    test_puntos_art()
    test_informe()
    
if __name__ == "__main__":
    main()