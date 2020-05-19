import unittest
from solution import findMin


class findMinTestCase(unittest.TestCase):
    def test_findMin_check1(self):
        result = findMin(1150,1)
        self.assertEqual(result,{'Output': [{'region': 'New York', 'total_cost': '$10150', 'machines': [('Large', 1), ('XLarge', 1), ('8XLarge', 7)]}, {'region': 'India', 'total_cost': '$10160', 'machines': [('Large', 3), ('8XLarge', 7)]}, {'region': 'China', 'total_cost': '$10150', 'machines': [('Large', 1), ('XLarge', 1), ('8XLarge', 7)]}]})

    def test_findMin_check2(self):
        result = findMin(850,1)
        self.assertEqual(result,{'Output': [{'region': 'New York', 'total_cost': '$7570', 'machines': [('Large', 1), ('2XLarge', 1), ('8XLarge', 5)]}, {'region': 'India', 'total_cost': '$7570', 'machines': [('Large', 1), ('2XLarge', 1), ('8XLarge', 5)]}, {'region': 'China', 'total_cost': '$7580', 'machines': [('Large', 1), ('XLarge', 2), ('8XLarge', 5)]}]})

    def test_findMin_check3(self):
        result = findMin(1100,12)
        self.assertEqual(result,{'Output': [{'region': 'New York', 'total_cost': '$118248', 'machines': [('XLarge', 1), ('2XLarge', 1), ('4XLarge', 1), ('8XLarge', 6)]}, {'region': 'India', 'total_cost': '$118368', 'machines': [('Large', 2), ('2XLarge', 1), ('4XLarge', 1), ('8XLarge', 6)]}, {'region': 'China', 'total_cost': '$118368', 'machines': [('XLarge', 3), ('4XLarge', 1), ('8XLarge', 6)]}]})



if __name__ == '__main__':
    unittest.main()
