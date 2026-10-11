class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # convert list to set
        nums_set = set(nums)
        # make result
        result = 0

        # for every element check if n - 1 exists
        for n in nums_set:
            # if it doesn't, check its sequence
            if n - 1 not in nums_set:
                temp_result = []
                temp_n = n
                while temp_n in nums_set:
                    temp_result.append(temp_n)
                    temp_n += 1

                # if len is greater than rsf, swap
                if (len(temp_result) > result):
                    result = len(temp_result)



        # return result
        return result

