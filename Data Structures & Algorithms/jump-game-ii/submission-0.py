# input
    # array of integers nums
        # nums[i] tells us the max length of a jump from its position i
        # you can jump to any value of i + j
            # j <= nums[i]
                # if nums[i] = 3, j = 1,2,3
            # i + j < nums.length

    # might perform traversal, hashmaps, two pointers, sliding window, dp, greedy

    # decision tree -> dp, greedy

    # will be positioned at nums[0]
        # we may have to start iteration starting from 0?
        # BUT this isn't guranteed

# task: return the min number of jumps to reach the last position
    # min number -> greedy

# assumptions: there is always a valid answer
    # we don't have test for cases where its not possible


# question: 
    # is it still valid if i go over the last index? NO
    # can there be a negative jump?
    # what is the range of nums length
    # what is the range of nums[i]

# example
    # [2,4,1,1,1,1]

    # from 2, we can jump 1 or 2
        # reach 4 
        # reach 1  # at each iteration, how we determine which path to go?

    # from 4, we can jump 1,2,3,4 
        # reach 1

# problem with my brute force solution: to start at 0, always reach the position where the max next jump exists
    # problem is, what if we don't reach the exact end index
    # ex) [2,3,1,3]

    # wrong, because even though we have jump value of 2, we can still jump 1

# base case: if the val + currentIndex <= last index




class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # use a pointer to keep currentIndex
        # starting at 0, we iterate

            # 1. go through all of its possible jumps
            # 2. find the corresponding next jump
            # 3. find which is the max

            # 4. take that max jump

        currentIndex = 0
        jumps = 0

        while currentIndex < len(nums) - 1:
            
            currentVal = nums[currentIndex]

            if currentIndex + currentVal >= len(nums) -1:
                jumps += 1
                break

            currentMax = [0, -1]

            for i in range(1, currentVal + 1):
                jumpVal = currentIndex + i + nums[currentIndex + i]
                if jumpVal > currentMax[1]:
                    currentMax[1] = jumpVal
                    currentMax[0] = currentIndex + i
            jumps += 1
            currentIndex = currentMax[0]
        return jumps
        
















        





