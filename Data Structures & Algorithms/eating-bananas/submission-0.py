class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force:
        # perform linear iteration. for each step, calculate 
            # math.ceil(val / k)

        # perform a binary search on k 

        # what is the lower and upper bound of k
            # lower = 1
            # upper = max pile value

        left = 1
        right = max(piles)
        ksf = right

        while left <= right:
            mid = (left + right) // 2

            if self.isValid(mid, piles, h):
                print(mid)
                print(ksf)
                ksf = min(ksf, mid)
                right = mid - 1

            else:
                left = mid + 1

        return ksf 

        


    def isValid(self, k, piles, h):
        hours = 0
        for p in piles:
            hours += math.ceil(p / k)
        return hours <= h


