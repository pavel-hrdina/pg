import unittest

from fourth import je_tah_mozny


class TestSachoveTahy(unittest.TestCase):
    def setUp(self):
        self.obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    def test_pesec(self):
        pesec = {"typ": "pěšec", "pozice": (2, 2)}
        self.assertTrue(je_tah_mozny(pesec, (3, 2), self.obsazene_pozice))
        self.assertFalse(je_tah_mozny(pesec, (4, 2), self.obsazene_pozice))
        self.assertFalse(je_tah_mozny(pesec, (1, 2), self.obsazene_pozice))

    def test_jezdec(self):
        jezdec = {"typ": "jezdec", "pozice": (3, 3)}
        self.assertFalse(je_tah_mozny(jezdec, (4, 4), self.obsazene_pozice))
        self.assertFalse(je_tah_mozny(jezdec, (5, 4), self.obsazene_pozice))
        self.assertTrue(je_tah_mozny(jezdec, (1, 2), self.obsazene_pozice))
        self.assertFalse(je_tah_mozny(jezdec, (9, 3), self.obsazene_pozice))

    def test_dama(self):
        dama = {"typ": "dáma", "pozice": (8, 3)}
        self.assertFalse(je_tah_mozny(dama, (8, 1), self.obsazene_pozice))
        self.assertFalse(je_tah_mozny(dama, (1, 3), self.obsazene_pozice))
        self.assertTrue(je_tah_mozny(dama, (3, 8), self.obsazene_pozice))

    def test_kral(self):
        kral = {"typ": "král", "pozice": (1, 4)}
        self.assertTrue(je_tah_mozny(kral, (2, 4), self.obsazene_pozice))
        self.assertTrue(je_tah_mozny(kral, (2, 5), self.obsazene_pozice))
        self.assertFalse(je_tah_mozny(kral, (3, 4), self.obsazene_pozice))


if __name__ == "__main__":
    unittest.main()
