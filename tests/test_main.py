import unittest
import numpy as np
from collections.abc import Mapping

from main_packg.main import hello_world, get_environment_variables, calculate_stats


class TestMain(unittest.TestCase):

    def test_hello_world(self):
        """Тестує, чи функція hello_world правильно повертає рядок."""
        self.assertEqual(hello_world(), "Hello, World!")

    def test_get_environment_variables(self):
        """Тестує, чи функція get_environment_variables повертає словник."""
        env_vars = get_environment_variables()
        self.assertIsInstance(env_vars, Mapping)
        # Перевірка на наявність конкретної змінної середовища (наприклад, HOME)
        self.assertIn('HOME', env_vars)
        
    def test_calculate_stats(self):
        data = np.array([1, 2, 3, 4, 5])
        mean, std_dev = calculate_stats(data)
        self.assertAlmostEqual(mean, 3.0, places=2)
        self.assertAlmostEqual(std_dev, 1.41, places=2)


if __name__ == '__main__':
    unittest.main()
