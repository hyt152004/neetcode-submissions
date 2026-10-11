class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        result = []

        postfix = []
        postfix_rsf = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_rsf = nums[i] * postfix_rsf
            postfix = [postfix_rsf] + postfix

  

        for i, value in enumerate(nums):
            if i + 1 >= len(nums):
                right = 1

            else:
                right = postfix[i + 1]

            result.append(left * right)
            left *= value

        
        return result