import unittest 
from diagnostico import CompuTools

class TestDiagnostico(unittest.TestCase):
    def test_is_sorted(self):
        compu = CompuTools()
        self.assertTrue(compu.is_sorted([1,2,3,4]))

    def test_is_not_sorted(self):
        compu = CompuTools()
        self.assertFalse(compu.is_sorted([3,4,1,2]))

if __name__ == "__main__":
    unittest.main()