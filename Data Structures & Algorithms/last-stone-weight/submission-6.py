class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        self.minHeap = []
        for stone in stones:
            self.minHeap.append(-stone)

        heapq.heapify(self.minHeap)

        while len(self.minHeap) > 1:

            stone_1 = - heapq.heappop(self.minHeap)
            stone_2 = - heapq.heappop(self.minHeap)

            if stone_1 != stone_2:
                heapq.heappush(self.minHeap, -(stone_1 - stone_2))

        
        if not len(self.minHeap):
            return 0
        return -self.minHeap[0]
        