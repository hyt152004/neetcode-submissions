class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for every value in nums, we have two paths
            # include the number and move on or exclude

        result = []

        subset = []

        def dfs(i):

            if (i >= len(nums)):
                result.append(subset.copy())
                print(subset)
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result

            
            