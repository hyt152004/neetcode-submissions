class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # use two pointers 
        left = 0
        right = 1
        rsf = 0

        while right < len(prices):
            

            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                rsf = max(rsf, profit)

            else:
                left = right


            right += 1

        return rsf