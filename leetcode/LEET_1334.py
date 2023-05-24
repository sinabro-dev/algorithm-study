"""
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.
Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.
Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
"""
class Solution:
    """
    Keyword: Floyd, DP
    Space: O(V^2)
    Time: O(V^3)
    """
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 그래프 상의 모든 노드끼리의 최소 거리를 모두 구해야하므로, 플로이드 알고리즘 활용.
        # 이때 메모 용도의 리스트는 1개로 한정, in-place 교체하여 리소스 절약 가능.

        memo = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            memo[i][i] = 0
        for edge in edges:
            start, end, cost = edge[0], edge[1], edge[2]
            memo[start][end] = cost
            memo[end][start] = cost
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    memo[i][j] = min(memo[i][j], memo[i][k]+memo[k][j])
        
        city = -1
        min_cnt = n

        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and memo[i][j] <= distanceThreshold:
                    cnt += 1
            
            if cnt <= min_cnt:
                city = i
                min_cnt = cnt

        return city
