class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1


        length = len(hm.values())
        valueResult = list(sorted(hm.values()))[length - k:length]

        result = []

        for key, value in hm.items():
            if value in valueResult:
                result.append(key)


        return result




