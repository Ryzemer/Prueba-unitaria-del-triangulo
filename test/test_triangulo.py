import unittest
from src.triangulo import area_triangulo


class TestAreaTriangulo(unittest.TestCase):

    def test_area_valida(self):
        self.assertAlmostEqual(area_triangulo(3, 4, 5), 6.0)
        self.assertAlmostEqual(area_triangulo(7, 10, 5), 16.24807680927192)

    def test_lados_invalidos(self):
        self.assertEqual(area_triangulo(1, 2, 3), "Los lados proporcionados no forman un triángulo válido.")
        self.assertEqual(area_triangulo(10, 1, 1), "Los lados proporcionados no forman un triángulo válido.")

    def test_lados_cero_ou_negativos(self):
        self.assertEqual(area_triangulo(0, 0, 0), "Los lados proporcionados no forman un triángulo válido.")
        self.assertEqual(area_triangulo(-1, -2, -3), "Los lados proporcionados no forman un triángulo válido.")


if __name__ == '__main__':
    unittest.main()
