import unittest

def solve(nums, target):
    freq = {}
    for i, num in enumerate(nums):
        if target - num in freq:
            return [freq[target - num], i]
        freq[num] = i

class TestClass(unittest.TestCase):
    def test_first(self):
        result = solve(nums = [2,7,11,15], target = 9)
        expected = [0,1]
        self.assertEqual(result, expected)
    def test_second(self):
        result = solve(nums = [3,2,4], target = 6)
        expected = [1,2]
        self.assertEqual(result, expected)
    def test_third(self):
        result = solve(nums = [3,3], target = 6)
        expected = [0,1]
        self.assertEqual(result, expected)