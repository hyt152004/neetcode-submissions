class Solution:
    def findMin(self, nums: List[int]) -> int:
        # idea: use binary search

        # for every midVal

            # 3 cases 

            # found if midVal < mid-1Val

            # mid > rightVal -> move left + 1

            # mid < right Val -> move right - 1

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]

            if midVal < nums[mid - 1]:
                return midVal

            elif midVal > nums[right]:
                left = mid + 1

            else:
                right = mid - 1

        return -1