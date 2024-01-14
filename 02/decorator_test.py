"""Tests for json_parser"""

import unittest
from unittest.mock import patch
import decorator


class TestFactorial(unittest.TestCase):

    def test_factorial(self):
        got_factorial = decorator.factorial(5)
        self.assertEqual(got_factorial, 120)
        got_factorial = decorator.factorial(1)
        self.assertEqual(got_factorial, 1)
        got_factorial = decorator.factorial(0)
        self.assertEqual(got_factorial, None)

    @patch.object(decorator, 'factorial')
    def test_callable(self, mock_factorial):
        decorator.compute_factorial(5)
        self.assertEqual(mock_factorial.call_count, 4)
        decorator.compute_factorial(10)
        self.assertEqual(mock_factorial.call_count, 13)

