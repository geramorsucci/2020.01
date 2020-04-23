import unittest
from sorting import Sort

class Test_Sorting (unittest.TestCase):
    def test_bubble_sort_one (self):
        lista = Sort().BubbleSort([36, 71, 16, 21, 73, 9, 0, 40, 66, 7])
        self.assertEqual(lista, [0,7,9,16,21,36,40,66,71,73])

    def test_bubble_sort_two (self):
        lista = Sort().BubbleSort([0, 2, 23, 4, 2, 8, 1, 25, 6, 9])
        self.assertEqual(lista, [0,1,2,2,4,6,8,9,23,25])

    def test_bubble_sort_three (self):
        lista = Sort().BubbleSort([5, 0, 15, 25, 21, 35, 40, 25, 6, 9])
        self.assertEqual(lista, [0,5,6,9,15,21,25,25,35,40])

if __name__ == '__main__':
    unittest.main()
