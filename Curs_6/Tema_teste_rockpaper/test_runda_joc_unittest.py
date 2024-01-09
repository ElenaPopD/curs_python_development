from Rock_paper_cod import runda_joc, piatra, foarfeca, hartie

import unittest

class TestRundaJoc(unittest.TestCase):

    def test_egalitate_runda(self):
        self.assertEqual(runda_joc(hartie, hartie), "Egalitate")
        self.assertEqual(runda_joc(piatra, piatra), "Egalitate")
        self.assertEqual(runda_joc(foarfeca, foarfeca), "Egalitate")

    def test_victorie_jucator1_runda(self):
        self.assertEqual(runda_joc(hartie, piatra), "Jucatorul 1 castiga")
        self.assertEqual(runda_joc(foarfeca, hartie), "Jucatorul 1 castiga")
        self.assertEqual(runda_joc(piatra, foarfeca), "Jucatorul 1 castiga")

    def test_victorie_jucator2_runda(self):
        self.assertEqual(runda_joc(piatra, hartie), "Jucatorul 2 castiga")
        self.assertEqual(runda_joc(hartie, foarfeca), "Jucatorul 2 castiga")
        self.assertEqual(runda_joc(foarfeca, piatra), "Jucatorul 2 castiga")

if __name__ == "__main__":
    unittest.main()
