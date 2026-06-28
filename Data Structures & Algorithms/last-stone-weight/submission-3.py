class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        print(heap)
        while len(heap) > 1 and heap:
            print(heap)
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            print(x, y)
            if x == y:
                continue
            
            if x < y:
                print(y - x)
                heapq.heappush(heap, -(y - x))

        if heap:
            return -heap[0]
        return 0