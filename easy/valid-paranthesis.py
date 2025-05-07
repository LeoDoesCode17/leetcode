import unittest
from collections import deque

def solve(s):
    # pair = {
    #     '(': ')',
    #     '{': '}',
    #     '[': ']',
    # }
    # stack = deque()
    # for char in s:
    #     if len(stack) == 0:
    #         stack.append(char)
    #     else:
    #         top = stack.pop()
    #         if top in pair and pair[top] != char:
    #             stack.append(top)
    #             stack.append(char)
    #         if not top in pair:
    #             stack.append(top)
    # return len(stack) == 0
    
    # optimized version    
    pair = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    stack = deque()
    for char in s:
        if char in pair:
            stack.append(char)
        else:
            if not stack or pair[stack.pop()] != char:
                return False
    return not stack
    

class TestClass(unittest.TestCase):
    def test_first(self):
        result = solve('()')
        expected = True
        self.assertEqual(result, expected)
    def test_second(self):
        result = solve('()[]{}')
        expected = True
        self.assertEqual(result, expected)
    def test_third(self):
        result = solve('(]')
        expected = False
        self.assertEqual(result, expected)
    def test_fourth(self):
        result = solve('([])')
        expected = True
        self.assertEqual(result, expected)