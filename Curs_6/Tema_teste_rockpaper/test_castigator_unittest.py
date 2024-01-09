from Rock_paper_cod import castigator,  hartie, piatra, foarfeca

import unittest


class TestCastigator(unittest.TestCase):

    def test_egalitate(self):
        self.assertEqual(castigator(hartie, hartie), 0)
        self.assertEqual(castigator(piatra, piatra), 0)
        self.assertEqual(castigator(foarfeca, foarfeca), 0)

    def test_castigator_jucator1(self):
        self.assertEqual(castigator(hartie, piatra), 1)
        self.assertEqual(castigator(foarfeca, hartie), 1)
        self.assertEqual(castigator(piatra, foarfeca), 1)

    def test_castigator_jucator2(self):
        self.assertEqual(castigator(piatra, hartie), 2)
        self.assertEqual(castigator(hartie, foarfeca), 2)
        self.assertEqual(castigator(foarfeca, piatra), 2)

if __name__ == "__main__":
    unittest.main()
