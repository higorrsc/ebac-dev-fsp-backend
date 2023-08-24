import unittest

from algorithms import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        unsorted_list = [66, 11, 4, 8, 1, 70]
        expected_list = [1, 4, 8, 11, 66, 70]
        unsorted_list = bubble_sort(unsorted_list)
        self.assertEqual(unsorted_list, expected_list)
