class Solution:
    def calculate_distance(self, x, y) -> float:
        return math.sqrt((x - 0) ** 2 + (y - 0) ** 2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        heap = []

        for point in points:
            dis = self.calculate_distance(point[0], point[1])
            heapq.heappush(heap, (dis, (point[0], point[1])))

        return [dp[1] for dp in heapq.nsmallest(k, heap)]