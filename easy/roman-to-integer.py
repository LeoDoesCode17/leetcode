import unittest

# command to run the test : python -m unittest "path to file relative to current directory"

# concept : if the next character has more value than the current, we have to combine it and count it (like IX, IV, XC, etc)
def solve(s: str) -> int:
    record = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    value = 1000
    result = 0
    for c in s:
        result += record[c]
        if value < record[c]:
            result -= 2*value
        value = record[c]
    return result

class TestClass(unittest.TestCase):
    def test_first(self):
        result = solve('III')
        expected = 3
        self.assertEqual(result, expected)
    def test_second(self):
        result = solve('LVIII')
        expected = 58
        self.assertEqual(result, expected)
    def test_third(self):
        result = solve('MCMXCIV')
        expected = 1994
        self.assertEqual(result, expected)