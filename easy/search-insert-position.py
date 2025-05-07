import unittest

# command to run the test : python -m unittest "path to file relative to current directory"
# Requirements : write the code using log(n) time complexity
# This can be done using binary search algorithm


def solve_recursive(nums, target):
    n = len(nums)
    
    # base case n == 1 or n == 2
    if n == 1:
        return int(target > nums[0])

    if n == 2:
        if target <= nums[0]:
            return 0
        elif target > nums[1]:
            return 2
        else:
            return 1

    l, r = 0, n - 1
    m = (l + r) // 2
    if nums[m] == target:
        return m
    elif nums[m] < target:
        l = m + 1
    else:
        r = m - 1

    return solve_recursive(nums[l:r+1], target) + l

def solve_iterative(nums, target):
    n = len(nums)
    idx = 0
    l, r = 0, n - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
            idx = l
        else:
            r = m - 1
        if r - l == 1:
            if target <= nums[l]:
                return idx
            elif target > nums[r]:
                return idx + 2
            else:
                return idx + 1
    return idx + 1 if nums[l] < target else idx

        

class TestClass(unittest.TestCase):
    def test_first_recursive(self):
        result = solve_recursive(nums=[1, 3, 5, 6], target=5)
        expected = 2
        self.assertEqual(result, expected)
        
    def test_first_iterative(self):
        result = solve_iterative(nums=[1, 3, 5, 6], target=5)
        expected = 2
        self.assertEqual(result, expected)

    def test_second_recursive(self):
        result = solve_recursive(nums=[1, 3, 5, 6], target=2)
        expected = 1
        self.assertEqual(result, expected)
        
    def test_second_iterative(self):
        result = solve_iterative(nums=[1, 3, 5, 6], target=2)
        expected = 1
        self.assertEqual(result, expected)

    def test_third_recursive(self):
        result = solve_recursive(nums=[1, 3, 5, 6], target=7)
        expected = 4
        self.assertEqual(result, expected)
        
    def test_third_iterative(self):
        result = solve_iterative(nums=[1, 3, 5, 6], target=7)
        expected = 4
        self.assertEqual(result, expected)

    def test_fouth_recursive(self):
        result = solve_recursive(nums=[1], target=0)
        expected = 0
        self.assertEqual(result, expected)
        
    def test_fouth_iterative(self):
        result = solve_iterative(nums=[1], target=0)
        expected = 0
        self.assertEqual(result, expected)
