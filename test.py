import unittest
from kal import Kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.kalkulator=Kalkulator()

    def test_dodaj(self):
        self.assertEqual(self.kalkulator.dodaj(10, 5), 15)
        self.assertEqual(self.kalkulator.dodaj(-1, 1), 0)
        self.assertEqual(self.kalkulator.dodaj(-1, -1), -2)

    def test_odejmij(self):
        self.assertEqual(self.kalkulator.odejmij(10, 5), 5)
        self.assertEqual(self.kalkulator.odejmij(-1, 1), -2)
        self.assertEqual(self.kalkulator.odejmij(-1, -1), 0)

    def test_pomnoz(self):
        self.assertEqual(self.kalkulator.pomnoz(10, 5), 50)
        self.assertEqual(self.kalkulator.pomnoz(-1, 1), -1)
        self.assertEqual(self.kalkulator.pomnoz(-1, -1), 1)

    def test_dziel(self):
        self.assertEqual(self.kalkulator.dziel(10, 5), 2)
        self.assertEqual(self.kalkulator.dziel(-1, 1), -1)
        self.assertEqual(self.kalkulator.dziel(-1, -1), 1)
        self.assertEqual(self.kalkulator.dziel(5, 2), 2.5)

        with self.assertRaises(ValueError):
            self.kalkulator.dziel(10, 0)


if __name__ == '__main__':
    unittest.main()
