class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # move the smaller side 

        leftP = 0
        rightP = len(heights) - 1
        rsf = 0

        while leftP < rightP:
            # calculate the volume 
            leftV = heights[leftP]
            rightV = heights[rightP]
            volume = min(leftV, rightV) * (rightP - leftP)

            # update rsf
            rsf = max(rsf, volume)

            # update pointer
            if leftV < rightV:
                leftP += 1
            else:
                rightP -= 1

        return rsf