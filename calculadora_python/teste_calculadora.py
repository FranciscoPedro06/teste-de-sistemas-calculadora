import unittest
from calculadora import somar, subtrair, multiplicar, dividir


class TestSoma(unittest.TestCase):

    def test_soma_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(somar(-2, -3), -5)

    def test_soma_misto(self):
        self.assertEqual(somar(-2, 3), 1)

    def test_soma_com_zero(self):
        self.assertEqual(somar(5, 0), 5)

    def test_soma_decimal(self):
        self.assertAlmostEqual(somar(2.5, 3.1), 5.6)

    def test_soma_grandes(self):
        self.assertEqual(somar(1000000, 2000000), 3000000)


class TestSubtracao(unittest.TestCase):

    def test_subtracao_positivos(self):
        self.assertEqual(subtrair(5, 3), 2)

    def test_subtracao_resultado_negativo(self):
        self.assertEqual(subtrair(3, 5), -2)

    def test_subtracao_com_zero(self):
        self.assertEqual(subtrair(5, 0), 5)

    def test_subtracao_decimal(self):
        self.assertAlmostEqual(subtrair(5.5, 2.2), 3.3)

    def test_subtracao_grandes(self):
        self.assertEqual(subtrair(5000000, 1000000), 4000000)


class TestMultiplicacao(unittest.TestCase):

    def test_multiplicacao_positivos(self):
        self.assertEqual(multiplicar(4, 3), 12)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(multiplicar(5, 0), 0)

    def test_multiplicacao_negativos(self):
        self.assertEqual(multiplicar(-4, 3), -12)

    def test_multiplicacao_decimal(self):
        self.assertAlmostEqual(multiplicar(2.5, 2), 5.0)

    def test_multiplicacao_grandes(self):
        self.assertEqual(multiplicar(100000, 1000), 100000000)


class TestDivisao(unittest.TestCase):

    def test_divisao_normal(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_divisao_decimal(self):
        self.assertAlmostEqual(dividir(5, 2), 2.5)

    def test_divisao_negativos(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_divisao_com_zero_no_dividendo(self):
        self.assertEqual(dividir(0, 5), 0)

    def test_divisao_grandes(self):
        self.assertEqual(dividir(1000000, 10), 100000)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)


if __name__ == "__main__":
    unittest.main()