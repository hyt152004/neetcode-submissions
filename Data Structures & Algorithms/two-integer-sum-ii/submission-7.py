class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        # for every int n 
        for i, n in enumerate(numbers):
            # if it exists using binary search
            value_to_find = target - n

            result = self.binarySearch(value_to_find, numbers)

            if result != -1:
                # return the two index
                return [i + 1, result + 1]




     
        return []


    def binarySearch(self, target, numbers):
        left = 0
        right = len(numbers) - 1

        while left <= right:
            middle = int((right + left) / 2)

            if numbers[middle] == target:
                return middle

            if numbers[middle] > target:
                right -= 1

            elif numbers[middle] < target:
                left += 1


        return -1




