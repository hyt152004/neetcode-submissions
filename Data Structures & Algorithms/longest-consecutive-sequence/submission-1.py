class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        rsf = 0

        for n in nums:
            if n - 1 not in nums_set:
                count = 0
                val = n
                while val in nums_set:
                    count += 1
                    val += 1
                    print(val)
                rsf = max(rsf, count)

        return rsf
                











