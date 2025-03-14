import unittest

# command to run the test : python -m unittest "path to file relative to current directory"

# Task : find the first index where the needle occurs in the haystack
# Idea : if given character is same as the needle, slice haystack with the length of the needle starting from the current index
def solve(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    n = len(haystack)
    m = len(needle)
    for i in range(n):
        if haystack[i] == needle[0]:
            lastIdx = i + m
            subArr = haystack[i:lastIdx]
            if subArr == needle:
                return i
    return -1

class TestClass(unittest.TestCase):
    def test_first(self):
        result = solve("sadbutsad", "sad")
        expected = 0
        self.assertEqual(result, expected)
    def test_second(self):
        result = solve("leetcode", "leeto")
        expected = -1
        self.assertEqual(result, expected)
    def test_third(self):
        result = solve("mississippi", "issip")
        expected = 4
        self.assertEqual(result, expected)

print(solve('hello', 'll'))