class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x2 = y2 = 0
        points = sorted(points, key = lambda x:math.sqrt(pow(x[0] - x2, 2) + pow(x[1] - y2, 2)))
        return points[:k]
