class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        # question:
        # return [] if no triplets found?
        # will there always be at least one triplet?
        # what is the range of the len(nums)
        # what is the range of int in nums?


        # idea:
        # sort the array 
        # [-1,0,1,2,-1,-4]
        # [-4,-1,-1,0,1,2]
            # target 4
        # for each num:
            # operate a two sum with the list that doesn't have the current num

        # ex
        # num is -1 
        # updated_array = [0,1,2,-1,-4]
        # operate a two sum with -(-1) being the target

        result = []
        # sort the array
        nums.sort()
        sort_nums = nums



        # [-4,-1,-1,0,1,2]

        # loop through the array
        for i, num in enumerate(sort_nums):
            if num > 0:
                break

            if i > 0 and num == sort_nums[i - 1]:
                continue
            # make the negation of current number the target
            target = -num

            # run a two sum to check if there is a triplet
            # we will only check for values to the right of i
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # Vleft + Vright == target
                    # update both left and right to contine checking for more
                    # also need to check if this combo is already in the result
                # Vleft + Vright > target
                    # move right pointer
                    # also make sure to continue duplicates
                # Vleft + Vright < target
                    # move left pointer
                    # also make sure to continue duplicates

                Vleft = sort_nums[left]
                Vright = sort_nums[right]

                if Vleft + Vright == target:
                    # TODO check for duplicate combo
                    if [num, Vleft, Vright] not in result:
                    # print('hlo')
                        result.append([num, Vleft, Vright])
                    left += 1
                    right -= 1
                elif Vleft + Vright > target:
                    right -= 1
                else:  
                    left += 1

        return result







