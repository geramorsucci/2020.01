import unittest
from punto import Punto2D, PuntoMejorado
from parameterized import parameterized

class TestPunto(unittest.TestCase):
    @parameterized.expand([(4, 5, "(4, 5)")])
    def test_str_punto(self, x, y, string):
        punto = Punto2D(x,y)
        self.assertEqual(punto.__str__(), string)

if __name__ == "__main__":
    unittest.main()