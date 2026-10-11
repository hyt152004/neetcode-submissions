class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # use a hashmap to track all the ones we've seen

        # based on the ones we've seen, try to see if  target - currentNum exists

        # num : index
        seenMap = {}

        for i, n in enumerate(nums):
            if target - n in seenMap:
                return [seenMap[target-n], i]

            seenMap[n] = i

        return 