import unittest
from customlist import *


class CustomListTest(unittest.TestCase):
    def setUp(self):
        self.test_custom_list = CustomList([])
        self.test_custom_list_2 = CustomList([])

    def test_add(self):
        result = CustomList([1, -7, 6, 6])
        self.test_custom_list.custom_list = [1, 2, 3, 6]
        self.test_custom_list_2.custom_list = [0, -9, 3]
        self.assertEqual((self.test_custom_list + self.test_custom_list_2), result)

        result.custom_list = [20, -11, -3]
        self.test_custom_list.custom_list = [9, -2]
        self.test_custom_list_2.custom_list = [11, -9, -3]
        self.assertEqual((self.test_custom_list + self.test_custom_list_2), result)

        result.custom_list = [10, -1, 10]
        self.test_custom_list.custom_list = [9, -2, 9]
        test_list = [1, 1, 1]
        self.assertEqual((self.test_custom_list + test_list), result)

    def test_sub(self):
        result = CustomList([1, 11, 0, 6])
        self.test_custom_list.custom_list = [1, 2, 3, 6]
        self.test_custom_list_2.custom_list = [0, -9, 3]

        self.assertEqual((self.test_custom_list - self.test_custom_list_2), result)

        result.custom_list = [-1, -11, 0, -6]
        self.assertEqual((self.test_custom_list_2 - self.test_custom_list), result)

        result.custom_list = [-10, 7, 9, 6]
        test_list = [1, 1, 1]
        self.test_custom_list.custom_list = [-9, 8, 10, 6]
        self.assertEqual((self.test_custom_list - test_list), result)

        result.custom_list = [10, -7, -9, -6]
        self.assertEqual((test_list - self.test_custom_list), result)

    def test_eq(self):
        self.test_custom_list.custom_list = [1, 2, 3, 6]
        self.test_custom_list_2.custom_list = [0, -9, 3]
        assert (self.test_custom_list == self.test_custom_list_2, False)

        self.test_custom_list_2.custom_list = [1, 2, 3, 6]
        assert (self.test_custom_list == self.test_custom_list_2, True)

    def test_ne(self):
        self.test_custom_list.custom_list = [1, 2, 3, 6]
        self.test_custom_list_2.custom_list = [0, -9, 3]
        assert (self.test_custom_list != self.test_custom_list_2, True)

        self.test_custom_list_2.custom_list = [1, 2, 3, 6]
        assert (self.test_custom_list == self.test_custom_list_2, False)


    def test_lt(self):
        self.test_custom_list.custom_list = [1, 2, 3, 6]
        self.test_custom_list_2.custom_list = [0, -9, 3]
        assert (self.test_custom_list < self.test_custom_list_2, False)
        assert (self.test_custom_list_2 < self.test_custom_list, True)

    def test_le(self):
        self.test_custom_list.custom_list = [1, 2, 3, 6]
        self.test_custom_list_2.custom_list = [0, -9, 3]
        assert (self.test_custom_list <= self.test_custom_list_2, False)

        self.test_custom_list.custom_list = [0, -9, 3]
        assert (self.test_custom_list_2 < self.test_custom_list, True)

    def test_gt(self):
        self.test_custom_list.custom_list = [1, 2, 3, 6]
        self.test_custom_list_2.custom_list = [0, -9, 3]
        assert (self.test_custom_list > self.test_custom_list_2, True)
        assert (self.test_custom_list_2 > self.test_custom_list, False)

    def test_arithmetic(self):
        self.test_custom_list.custom_list = [1, 2, 3]
        result_list = [0, 0, 0]
        arithmetic_result = self.test_custom_list.arithmetic_operation([-1, -2, -3], '+')
        self.assertEqual(arithmetic_result, result_list)

    def test_ge(self):
        self.test_custom_list.custom_list = [1, 2, 3, 6]
        self.test_custom_list_2.custom_list = [0, -9, 3]
        assert (self.test_custom_list > self.test_custom_list_2, True)

        self.test_custom_list.custom_list = [0, -9, 3]
        assert (self.test_custom_list_2 >= self.test_custom_list, True)

        self.test_custom_list.custom_list = [0, 100, 3]
        assert (self.test_custom_list_2 >= self.test_custom_list, False)



