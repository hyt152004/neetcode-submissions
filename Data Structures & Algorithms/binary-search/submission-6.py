class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # using the left and right pointer find the current length
        # find the middle value
            # cases
            # its equal -> return
            # less than target -> look at left portion
            # greater than target -> look at right portion


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            midVal = nums[mid]
            print(midVal)

            if midVal == target:
                return mid

            elif midVal < target:
                left = mid + 1
                
            else:
                right = mid - 1
            

        return -1






