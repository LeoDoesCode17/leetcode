import unittest

# Algorithm: Two Pointers algorithm
# Time Complexity : O(N)

def solve(x):
    # string1 = str(x)
    # return string1 == string1[::-1]
    if x < 0:
        return False
    numberStr = str(x)
    l, r = 0, len(numberStr) - 1
    while l < r:
        if numberStr[l] != numberStr[r]:
            return False
        l += 1
        r -= 1
    return True

class TestClass(unittest.TestCase):
    def test_first(self):
        result = solve(121)
        expected = True
        self.assertEqual(result, expected)
    def test_second(self):
        result = solve(-121)
        expected = False
        self.assertEqual(result, expected)
    def test_third(self):
        result = solve(10)
        expected = False
        self.assertEqual(result, expected)