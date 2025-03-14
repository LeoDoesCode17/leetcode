import unittest

def solve(strs):
    MAX_LEN = 200
    minLen = MAX_LEN
    shortestString = ""

    # If there is only one string in strs
    if len(strs) == 1:
        return strs[0]

    # Find the shortest string in strs
    for str in strs:
        if minLen > len(str):
            minLen = len(str)
            shortestString = str

    if minLen == 0:
        return ""
        
    maxIdx = -1

    # Find the longest common prefix
    for i in range(minLen):
        commonChar = strs[0][i]
        for str in strs:
            if str[i] != commonChar:
                if maxIdx == -1:
                    return ""
                else:
                    return shortestString[:maxIdx+1]
        maxIdx = i

    return shortestString[:maxIdx+1]
            

class TestClass(unittest.TestCase):
    def test_first(self):
        result = solve(["flower","flow","flight"])
        expected = "fl"
        self.assertEqual(result, expected)
    def test_second(self):
        result = solve(["dog","racecar","car"])
        expected = ""
        self.assertEqual(result, expected)
    def test_third(self):
        result = solve(["a"])
        expected = "a"
        self.assertEqual(result, expected)
        
    