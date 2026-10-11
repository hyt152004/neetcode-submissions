class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lsf = 101
        biggest_profit = 0

        for i in prices:
            if i < lsf:
                lsf = i

            else:
                if (i - lsf > biggest_profit):
                    biggest_profit = i - lsf

        return biggest_profit