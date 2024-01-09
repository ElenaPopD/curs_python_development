import unittest

class TestExample(unittest.TestCase):

    def setUp(self):
        print("In Setup")
        self.value_to_test = True

    def test_1(self):
        print("In test 1")
        self.assertTrue(self.value_to_test)

    def test_2(self):
        print("In test 2")
        self.assertTrue(self.value_to_test)

    def test_3(self):
        print("In test 3")
        self.assertTrue(self.value_to_test)

    def tearDown(self):
        print("In Teardown")
        self.value_to_test = False

    def setUpClass():
        print("Setting up class")

    def tearDownClass():
        print("Tearing down class")