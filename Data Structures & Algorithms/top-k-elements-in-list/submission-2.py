class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort method

        # find the number of occurrances
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1

        # build the buckets
        # index is the # of occurrances
        # value is the value of the repeated value

        # make an array of length len(nums) since at worst case, all nums will be unique
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])  

        for key, value in hm.items():
            bucket[value].append(key)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result


     


        






