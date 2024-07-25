from Dijkstra import dijkstra_gas_consumption

import unittest

class TestDijkstraGasConsumption(unittest.TestCase):
    def setUp(self):
    # Configuración de los datos para los tests
        self.road_network = {
            'A': [('B', 10, 5), ('C', 15, 10)],
            'B': [('D', 12, 3), ('E', 15, 7)],
            'C': [('E', 10, 2)],
            'D': [('F', 1, 0)],
            'E': [('F', 5, 1)],
            'F': []
        }
        self.start_city = 'A'
        self.end_city = 'F'
        self.initial_velocity = 60  # km/h
        self.gasoline_consumption_per_km = 0.05  # liters per km
        self.initial_gasoline = 20  # liters
        self.max_time_extension_factor = 1.5

    def test_shortest_path(self):

        road_network = {
            'Caracas': [('Maracay', 120, 5)],
            'Maracay': [('Caracas', 120, 5), ('Valencia', 80, -2)],
            'Valencia': [('Maracay', 80, -2), ('Merida', 180, 3)],
            'Merida': [('Valencia', 180, 3)]
        }

        initial_velocity = 40  # km/h
        gasoline_consumption_per_km = 0.1  # litros
        initial_gasoline = 40  # litros
        max_time_extension_factor = 1.2

        start_city = 'Caracas'
        end_city = 'Merida'
        fuel_used, shortest_time = dijkstra_gas_consumption(
            road_network, start_city, end_city, 
            initial_velocity, gasoline_consumption_per_km, 
            initial_gasoline, max_time_extension_factor
        )
        
        self.assertAlmostEqual(shortest_time, 9.5, places=1)
        self.assertAlmostEqual(fuel_used, 38.8, places=0)

    def test_no_route_possible_due_to_gasoline_limit(self):
    # Test cuando no hay suficiente gasolina
        limited_gasoline = 1  # litros, insuficiente para llegar al destino
        cost, time = dijkstra_gas_consumption(self.road_network, self.start_city, self.end_city, self.initial_velocity, self.gasoline_consumption_per_km, limited_gasoline, self.max_time_extension_factor)
        self.assertIsNone(cost)
        self.assertIsNone(time)
    
    def test_no_route_possible_due_to_time_limit(self):
        # Test cuando no se puede llegar debido a la limitación de tiempo
        limited_time_extension_factor = 0.1  # Factor de extensión de tiempo muy bajo
        cost, time = dijkstra_gas_consumption(self.road_network, self.start_city, self.end_city, self.initial_velocity, self.gasoline_consumption_per_km, self.initial_gasoline, limited_time_extension_factor)
        self.assertIsNone(cost)
        self.assertIsNone(time)

if __name__ == '__main__':
    unittest.main()