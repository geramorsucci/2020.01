import unittest
from listas import listas

class BubbleSortTest(unittest.TestCase):
    def testArray1(self):
        ls1 = [36, 71, 16, 21, 73, 9, 0, 40, 66, 7]
        bubble1 = listas().BubbleSort(ls1)
        self.assertEqual(ls1, bubble1)

    def testArray2(self):
        ls2 = [0, 2, 23, 4, 2, 8, 1, 25, 6, 9]
        bubble2 = listas().BubbleSort(ls2)
        self.assertEqual(ls2, bubble2)

    def testArray3(self):
        ls3 = [5, 0, 15, 25, 21, 35, 40, 25, 6, 9]
        bubble3 = listas().BubbleSort(ls3)
        self.assertEqual(ls3, bubble3)

if __name__=="__main__":
    unittest.main()

