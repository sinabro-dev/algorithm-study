"""
https://leetcode.com/problems/number-of-closed-islands/description/

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
Return the number of closed islands.

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
"""
class Solution:
    """
    Keyword: BFS
    Space: O(m)
    Time: O(nm)
    """
    def closedIsland(self, grid: List[List[int]]) -> int:
        # 각 요소에 대해 BFS로 0 값을 갖는 곳을 탐색
        # 더이상 탐색할 곳이 없을 때
        # 주변이 모두 1 값으로 둘러쌓여있을 때는 섬을 찾은 것이고
        # 그렇지 않은 경우 섬이 아닌 것

        n, m = len(grid), len(grid[0])

        island = 0
        visited = set()

        for r in range(n):
            for c in range(m):
                if grid[r][c] != 0:
                    continue
                
                if (r, c) in visited:
                    continue

                is_island = True
                queue = collections.deque()

                visited.add((r, c))
                queue.append((r, c))

                while queue:
                    i, j = queue.popleft()

                    if (i-1 < 0) or (i+1 >= n) or (j-1 < 0) or (j+1 >= m):
                        is_island = False

                    if (i-1 >= 0) and (grid[i-1][j] == 0) and ((i-1, j) not in visited):
                        visited.add((i-1, j))
                        queue.append((i-1, j))
                    if (i+1 < n) and (grid[i+1][j] == 0) and ((i+1, j) not in visited):
                        visited.add((i+1, j))
                        queue.append((i+1, j))
                    if (j-1 >= 0) and (grid[i][j-1] == 0) and ((i, j-1) not in visited):
                        visited.add((i, j-1))
                        queue.append((i, j-1))
                    if (j+1 < m) and (grid[i][j+1] == 0) and ((i, j+1) not in visited):
                        visited.add((i, j+1))
                        queue.append((i, j+1))
                
                if is_island:
                    island += 1
        
        return island
