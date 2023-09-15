"""
https://leetcode.com/problems/min-cost-to-connect-all-points/description/?envType=daily-question&envId=2023-09-15

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
- 1 <= points.length <= 1000
- 106 <= xi, yi <= 106
- All pairs (xi, yi) are distinct

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
"""
class Solution:
    """
    Keyword: MST, Kruskal
    Space: O(n^2)
    Time: (n^2)
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # MST 알고리즘 중 Kruskal 알고리즘을 이용하여 풀이

        from heapq import heappush, heappop

        n = len(points)

        distance_heap = list()
        for i in range(n):
            p1 = points[i]
            for j in range(i):
                p2 = points[j]
                distance = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
                heappush(distance_heap, (distance, i, j))

        parents = dict()
        for x, y in points:
            parents[(x, y)] = (x, y)

        def find(x, y: int) -> (int, int):
            parent = parents[(x, y)]
            if (x, y) != parent:
                parents[(x, y)] = find(parent[0], parent[1])
                parent = parents[(x, y)]
            return parent
            
        def union(x1, y1, x2, y2: int) -> None:
            parent1, parent2 = parents[(x1, y1)], parents[(x2, y2)]
            if parent1 == parent2:
                return
            parents[parent2] = parent1

        edge_cnt, cost = 0, 0
        while distance_heap:
            if edge_cnt == n-1:
                break
            
            distance, i, j = heappop(distance_heap)
            p1, p2 = points[i], points[j]

            if find(p1[0], p1[1]) != find(p2[0], p2[1]):
                union(p1[0], p1[1], p2[0], p2[1])
                edge_cnt += 1
                cost += distance
        
        return cost
