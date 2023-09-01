"""
https://leetcode.com/problems/rotting-oranges/description/?envType=daily-question&envId=2023-09-01

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2
 
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
"""
class Solution:
    """
    Keyword: BFS
    Space: O(max(m, n))
    Time: O(mn)
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS로 썩어있던 오렌지를 시점으로 탐색해가며 그 대상을 넓혀가고,
        # 최종적으로 모든 오렌지들을 훑었는지 확인

        from collections import deque

        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    grid[r][c] = 0
                    queue.append((r, c, 0))
        
        while queue:
            r, c, now = queue.popleft()

            if r+1 < rows and grid[r+1][c] == 1:
                grid[r+1][c] = -(now+1)
                queue.append((r+1, c, now+1))
            if c+1 < cols and grid[r][c+1] == 1:
                grid[r][c+1] = -(now+1)
                queue.append((r, c+1, now+1))
            if c-1 >= 0 and grid[r][c-1] == 1:
                grid[r][c-1] = -(now+1)
                queue.append((r, c-1, now+1))
            if r-1 >= 0 and grid[r-1][c] == 1:
                grid[r-1][c] = -(now+1)
                queue.append((r-1, c, now+1))
        
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
                time = max(time, -grid[r][c])
        
        return time
