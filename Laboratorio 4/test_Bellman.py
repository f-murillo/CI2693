import unittest
from Bellman import bellman_gas_consumption

class TestBellmanGasConsumption(unittest.TestCase):
    def setUp(self):
        self.road_network = {
            'Caracas': [('Maracay', 120, 5)],
            'Maracay': [('Caracas', 120, 5), ('Valencia', 80, -2)],
            'Valencia': [('Maracay', 80, -2), ('Merida', 180, 3)],
            'Merida': [('Valencia', 180, 3), ('Maracay', 80, -2)]
        }
        self.road_network_free = ['Maracay']
        self.start_city = 'Caracas'
        self.end_city = 'Merida'
        self.initial_velocity = 40
        self.gasoline_consumption_per_km = 0.1
        self.initial_gasoline = 40
        self.max_time_extension_factor = 1.2

    def test_shortest_path(self):
        fuel_used, shortest_time = bellman_gas_consumption(
            self.road_network, self.road_network_free, self.start_city, self.end_city,
            self.initial_velocity, self.gasoline_consumption_per_km, self.initial_gasoline,
            self.max_time_extension_factor
        )

        self.assertAlmostEqual(shortest_time, 9.5, places=1)
        self.assertAlmostEqual(fuel_used, 23.8, places=0)

    def test_no_route_possible_due_to_gasoline_limit(self):
        limited_gasoline = 1
        cost, time = bellman_gas_consumption(
            self.road_network, self.road_network_free, self.start_city, self.end_city,
            self.initial_velocity, self.gasoline_consumption_per_km, limited_gasoline,
            self.max_time_extension_factor
        )

        self.assertIsNone(cost)
        self.assertIsNone(time)

    def test_no_route_possible_due_to_time_limit(self):
        limited_time_extension_factor = 0.1
        cost, time = bellman_gas_consumption(
            self.road_network, self.road_network_free, self.start_city, self.end_city,
            self.initial_velocity, self.gasoline_consumption_per_km, self.initial_gasoline,
            limited_time_extension_factor
        )

        self.assertIsNone(cost)
        self.assertIsNone(time)

    def test_negative_cycle(self):
        road_network_with_negative_cycle = {
            'Caracas': [('Maracay', 120, 5)],
            'Maracay': [('Caracas', 120, 5), ('Valencia', 80, -2)],
            'Valencia': [('Maracay', 80, -2), ('Merida', 180, 3)],
            'Merida': [('Valencia', 180, 3), ('Maracay', 300, -2)]
        }
        road_network_free_with_negative_cycle = ['Merida']
        start_city_with_negative_cycle = 'Caracas'
        end_city_with_negative_cycle = 'Merida'
        initial_velocity_with_negative_cycle = 40
        gasoline_consumption_per_km_with_negative_cycle = 0.1
        initial_gasoline_with_negative_cycle = 40
        max_time_extension_factor_with_negative_cycle = 1.2

        with self.assertRaises(ValueError):
            bellman_gas_consumption(
                road_network_with_negative_cycle, road_network_free_with_negative_cycle,
                start_city_with_negative_cycle, end_city_with_negative_cycle,
                initial_velocity_with_negative_cycle, gasoline_consumption_per_km_with_negative_cycle,
                initial_gasoline_with_negative_cycle, max_time_extension_factor_with_negative_cycle
            )


if __name__ == '__main__':
    unittest.main()