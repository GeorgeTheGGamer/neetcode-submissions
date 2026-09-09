class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # How about I Have a min heap off distances and the the point with it
        min_heap = []
        result = []
        # Make min heap based on distances
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            heapq.heappush(min_heap, (distance,point[0],point[1]))
        
        # Trim the rest 
        while len(result) != k:
            result.append([min_heap[0][1],min_heap[0][2]])
            heapq.heappop(min_heap)
        
        return result

        