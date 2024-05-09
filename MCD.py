import unittest

def mcd(a, b):
    """
    Función para calcular el máximo común divisor de dos números.
    """
    while b:
        a, b = b, a % b
    return a

def mcd_four_numbers(a, b, c, d):
    """
    Función para calcular el máximo común divisor de cuatro números.
    """
    mcd_ab = mcd(a, b)
    mcd_cd = mcd(c, d)
    return mcd(mcd_ab, mcd_cd)

class TestMcd(unittest.TestCase):
    def test_mcd(self):
        # Pruebas para la función mcd
        self.assertEqual(mcd(12, 8), 4)
        self.assertEqual(mcd(17, 5), 1)
        self.assertEqual(mcd(50, 20), 10)

    def test_mcd_four_numbers(self):
        # Pruebas para la función mcd para 4 numeros
        
        self.assertEqual(mcd_four_numbers(12, 24, 36, 48), 12)
        self.assertEqual(mcd_four_numbers(15, 30, 45, 60), 15)
        self.assertEqual(mcd_four_numbers(18, 36, 54, 72), 18)

if __name__ == '__main__':
    unittest.main(),



