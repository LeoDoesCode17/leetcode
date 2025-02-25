from typing import List

# Concept : array
def removeElement(nums: List[int], val: int) -> int:
    tempList = [99] * len(nums)
    idx = 0
    for i in nums:
        if i == val:
            continue
        tempList[idx] = i
        idx += 1
    nums[:] = tempList
    return idx

myList = [3,2,2,3]
print(removeElement(nums=myList, val=3))
print(myList)