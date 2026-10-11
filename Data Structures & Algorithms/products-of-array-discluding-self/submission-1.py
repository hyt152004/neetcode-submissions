class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        result = []
        for i, value in enumerate(nums):
            temp_i = i + 1
            right = 1
            while temp_i < len(nums):
                right *= nums[temp_i]
                temp_i += 1

            result.append(left * right)
            left *= value

        
        return result