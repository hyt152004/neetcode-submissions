class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, value in enumerate(nums):
            subtract = target - value

            if subtract in hashmap:
                return [hashmap[subtract], i]

            hashmap[value] = i


        return None
    





        