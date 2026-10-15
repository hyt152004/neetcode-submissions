
# given as input 
    # integer array coins
    # integer amount

    # traversing?

# task:
    # return the num of distinct combinations that total up to amount
        # can not have duplicates
            # same order -> cache? 
    # if not possible, return 0
        # base case? -> if we reach the last element? perhaps even the one after the last?

# assumption: 
    # can use unlimited number of each coin 
        # can reuse coins -> may cause duplicates
        # the steps taken at each stage will be affecte
            # take -> take again
            # skip
    # each value in coins is unique
        # this may solve our worry of duplicates?

# questions:
    # what is the range of len(coins) -> small
    # what is the range of amount -> medium
    # can coins[i] be a negative? -> at least 1 -> we don't need to worry about inf 0's
    # can amount be negative? -> no


# example: amount = 4, coins = [1,2,3]
    # at coins[0] -> 1

    # case 1:
        # take -> amount - ith
        # try ith again

    # case 2:
        # skip -> try i+1th, amount = amount

    



# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         from functools import cache
#         @cache
#         def numWays_startingAt_ToReachAmount(i, x) -> int:
#             # base case
#             if i == len(coins):
#                 if x == 0:
#                     return 1

#                 return 0

#             if amount >= coins[i]:
#                 take = numWays_startingAt_ToReachAmount(i, x - coins[i])
#             skip = numWays_startingAt_ToReachAmount(i + 1, x)

#             return take + skip
#         return numWays_startingAt_ToReachAmount(0, amount)
        

from typing import List
from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def numWays_startingAt_ToReachAmount(i: int, x: int) -> int:
            # Base cases
            if x == 0:
                return 1
            if x < 0 or i == len(coins):
                return 0
                
            # Choice 1: Skip the current coin
            skip_coin = numWays_startingAt_ToReachAmount(i + 1, x)
            
            # Choice 2: Use the current coin (stay at index 'i' to allow reuse)
            use_coin = numWays_startingAt_ToReachAmount(i, x - coins[i])
            
            return skip_coin + use_coin
            
        return numWays_startingAt_ToReachAmount(0, amount)









        