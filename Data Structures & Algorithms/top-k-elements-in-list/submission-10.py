from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create an array that uses index as the freq and value as the list of num values

        # this array is one size larger than len(nums)

        freq = [[] for _ in range(len(nums) + 1)]

        counter = Counter(nums)

        for key, value in counter.items():
            freq[value].append(key)

        pointer = len(freq) - 1
        result = []
        while k > 0:
            for val in freq[pointer]:
                result.append(val)
                k -= 1
            pointer -= 1

        return result







