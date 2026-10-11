class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # question:
        # will there be at least 2 bars
        # what happens if no container can be formed?
        # can heights be empty?
        # can the height ever be negtative?


        # brute force:
        # find every pair of container, calculate its area, and find the max
        # time O(n^2)

        # idea: two pointer 
        # left (start at the beginning)
        # right (start at the end)

        # run a while loop (left < right)
        # calcute the area and check if greater than rsf
        # move the pointer at the smaller bar

        # two cases
        # one bar is smaller than other
            # move smaller bar
        # both bar are at same height
            # move the left pointer
            # idea: if two bars are at the same height, this height will restrict the next iteration area 
            # so it wouldn't matter

        rsf = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            # calcute the current area
            # need width (right - left)
            # need height (min beteen Vleft and Vright)

            width = right - left
            height = min(heights[left], heights[right])

            area = width * height

            rsf = max(rsf, area)

            if heights[left] == heights[right]:
                left += 1
            else:
                if heights[left] > heights[right]:
                    right -= 1
                else:
                    left += 1

        return rsf








        
        