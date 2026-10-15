# input:
    # integer array coins
    # integer amount 

    # traversal?
    # dp?

# task: 
    # find the fewest number of coins that you need to make up the EXACT target amount
        # need to think about previous calculation -> dp?

    # if not possible, return -1
        # base case?
            # when current x is negative
            # when we reach the end of array?

# assumption: 
    # can use the coin unlimited num of times

    # this breaks down the possibilities
        # take -> take again
        # skip 

# example:
    # coins = coins, amount = amount

    # take ith -> amount - ith -> amount - (i + 1th)
    # skip ith -> amount = amount -> i + 1th

    # we need to find the min of taking it or skipping it




from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def numCoins_startingAt_toReach(i, x) -> int:
            if i == len(coins):
                if x == 0:
                    return 0
                return float('inf')

            take = float('inf')
            if x >= coins[i]:
                take = 1 + numCoins_startingAt_toReach(i, x - coins[i])
            skip = numCoins_startingAt_toReach(i + 1, x)

            return min(skip, take)
        
        res = numCoins_startingAt_toReach(0, amount)
        return -1 if res == float('inf') else res








