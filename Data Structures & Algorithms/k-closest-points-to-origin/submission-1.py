class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math
        heap = []
        for x,y in points:
            print("x:{} and y:{}".format(x,y))
            distance = math.sqrt(x**2 + y**2)
            print(distance)

            heapq.heappush(heap, (distance, (x,y)))
        key_shortest = []
        for _ in range(k):
            distance, point = heapq.heappop(heap)
            key_shortest.append(point)

        return key_shortest



