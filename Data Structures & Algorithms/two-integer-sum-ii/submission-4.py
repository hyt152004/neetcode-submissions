from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            value_to_find = target - n
            result = self.binarySearch(value_to_find, numbers, i+1, len(numbers)-1)
            if result != -1:
                return [i + 1, result + 1]
        return []

    def binarySearch(self, target, numbers, left, right):
        while left <= right:
            middle = left + (right - left) // 2
            if numbers[middle] == target:
                return middle
            elif numbers[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
