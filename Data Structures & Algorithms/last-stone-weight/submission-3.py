class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Initialise the max heap
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            x = - heapq.heappop(max_heap)
            y = - heapq.heappop(max_heap)
            if y < x:           # Second is always going to be less than or equal to x, nature of max_heap
                heapq.heappush(max_heap, -(x-y))
        
        max_heap.append(0)
        return -max_heap[0]
        
        