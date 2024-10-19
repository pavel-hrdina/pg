import unittest

from third import je_prvocislo, vrat_prvocisla  # Import functions from third.py


class TestPrvocislaFunctions(unittest.TestCase):

    def test_je_prvocislo(self):
        # Test known prime numbers
        self.assertTrue(je_prvocislo(2))
        self.assertTrue(je_prvocislo(3))
        self.assertTrue(je_prvocislo(5))
        self.assertTrue(je_prvocislo(7))
        self.assertTrue(je_prvocislo(11))

        # Test known non-prime numbers
        self.assertFalse(je_prvocislo(1))
        self.assertFalse(je_prvocislo(4))
        self.assertFalse(je_prvocislo(9))
        self.assertFalse(je_prvocislo(12))
        self.assertFalse(je_prvocislo(36))

    def test_vrat_prvocisla(self):
        # Test with various maximum values
        self.assertEqual(vrat_prvocisla(10), [2, 3, 5, 7])
        self.assertEqual(vrat_prvocisla(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(vrat_prvocisla(1), [])
        self.assertEqual(vrat_prvocisla(0), [])


if __name__ == "__main__":
    unittest.main()
