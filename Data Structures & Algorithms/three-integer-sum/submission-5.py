class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = set()
        for i, target in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            seenMap = set()
            for j in range(i + 1, len(nums)):
                val = nums[j]

                neededVal = -(val + target)

                if neededVal in seenMap:
                    result.add((target, neededVal, val))

                seenMap.add(val)

        return [list(l) for l in result]

