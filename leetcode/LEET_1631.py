"""
https://leetcode.com/problems/path-with-minimum-effort/description/?envType=daily-question&envId=2023-09-16

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
- rows == heights.length
- columns == heights[i].length
- 1 <= rows, columns <= 100
- 1 <= heights[i][j] <= 106

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
"""
class Solution:
    """
    Keyword: Dijkstra
    Space: O(mn)
    Time:((m+n)log(m+n))
    """
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # DFS로 모든 경로를 훑으며 절대값 차가 가장 작은 경우를 찾음
        # 그러나 이렇게 하면 너무 많은 연산으로 시간 초과
        # 다익스트라 알고리즘으로 최소 비용 경로를 구해내야 함

        from heapq import heappush, heappop

        rows, cols = len(heights), len(heights[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        ans = 10**6

        dists = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        heap = list()
        heappush(heap, (0, 0, 0))

        while heap:
            effort, r, c = heappop(heap)

            if r == rows-1 and c == cols-1:
                return effort
            
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc

                if not (0<=nr<rows and 0<=nc<cols):
                    continue
                
                new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                if new_effort < dists[nr][nc]:
                    dists[nr][nc] = new_effort
                    heappush(heap, (new_effort, nr, nc))
