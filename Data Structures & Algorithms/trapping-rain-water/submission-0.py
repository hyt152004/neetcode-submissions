class Solution:
    def trap(self, height: List[int]) -> int:
        
        # brute force:
        # find water between each pair of bars
        # and subtract the area based on the inner bar heights


        # idea:
        # compute the maxLeft, maxRight, min array

        # create maxLeft
        # ex.
        # [0,2,0,3,1,0,1,3,2,1]
        # [0,0,2,2,3,3,3,3,3,3]

        # append itself
        # check if itself is greater than the maxLeftValue
        maxLeft = []
        maxLeftV = 0
        for num in height:
            maxLeft.append(maxLeftV)
            maxLeftV = max(num, maxLeftV)

        # create maxRight
        # ex.
        # [0,2,0,3,1,0,1,3,2,1]
        # [3,3,3,3,3,3,3,2,1,0]
        maxRight = []
        maxRightV = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight = [maxRightV] + maxRight
            maxRightV = max(height[i], maxRightV)

        # [0,0,2,2,3,3,3,3,3,3]
        # [3,3,3,3,3,3,3,2,1,0]
        # create min side 
        minSide = []
        for i in range(len(height)):
            minSide.append(min(maxLeft[i], maxRight[i]))
        # print(minSide)

        rsf = 0
        # now use the minSide array to calculate the area of water for each index
        for i, num in enumerate(height):
            # get the minSide value
            # do minSideV - num = water area
            # add this area to the rsf
            minSideV = minSide[i]
            waterArea = minSideV - num
            print(waterArea)
            if waterArea > 0:
                rsf += waterArea

        return rsf

