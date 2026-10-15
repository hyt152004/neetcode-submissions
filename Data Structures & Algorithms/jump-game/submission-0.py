#input integer array mums
    # num[i] tells you the max jump you can take from that position

# task: figure out if we can make it to the last index starting at index 0
    # if not, return false

# questions:
    # can there be a 0 jump?
    # what is the range of len(nums)?
    # can there be negative jumps?
    # what happens on the last jump?
    # it the last jump irrelevant?
        # why is it given to us?

# brute force:
    # starting from index 0, try every option
    # ex) [1,2,0,1,0]
        # 1 -> 2 -> 1 -> done
            # following the direct order works?
        # [2,1,2,0,0]
        # 2 -> 1 -> 2 -> done
        # 2 -> 2 -> done

        # at 2, we can either take 1 or 2
            # we have no skip option
        # at 1, can only take 1

# solution: try taking as advantage that the last jump is irelevant
    # base case: last index -> if on last index, we its always true


    # j = len(nums) - 1

    # from j, can i use any of the values before me to reach currentPosition?
        # use j - 1

    # from j - 1, can i use any of the values before me to reach j - 1?
        # use j - 3
    # from j - 3, can i use any of the values before me to reach j - 3?
        # use j - 4
        # reach 0 index -> done

    
    # we step when we reach the first index, or we looped through every value but couldn't find a jump


        

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        currentPosition = len(nums) - 1
        
        for j in range(len(nums) - 1, -1, -1):
            
            jVal = nums[j]

            if currentPosition <= j + jVal:
                currentPosition = j

        return currentPosition == 0


            




        