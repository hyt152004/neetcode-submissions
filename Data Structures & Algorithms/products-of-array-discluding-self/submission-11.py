class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefixVal = 1
        for i in range(len(nums)):
            result[i] *= prefixVal
            prefixVal *= nums[i]

        postfixVal = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfixVal
            postfixVal *= nums[i]

        return result

        # nums=[1,2,4,6]

        # [1, 2, 8, 48]
        # [48, 48, 24, 6]

        # [1 ]

        # multiple then update the array








