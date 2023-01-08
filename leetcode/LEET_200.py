"""
https://leetcode.com/problems/number-of-islands/submissions/873940817/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # return self.dfs_solution(grid)
        return self.find_union_solution(grid)
    
    """
    Keyword: DFS
    Space: O(N)
    Time: O(N^2)
    """
    def dfs_solution(self, grid: List[List[str]]) -> int:
        # 먼저 떠오른 방법은 `grid` 요소들을 반복 접근하여, 매 요소마다
        # 같은 값을 갖는 인접 요소에 BFS로 탐색 및 탐색 여부 저장함으로써
        # `1` 값을 갖는 그래프 탐색이 얼마나 있는지 확인하는 것.

        island_cnt = 0
        row_size = len(grid)
        col_size = len(grid[0])

        from collections import deque

        d_ij = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        d_size = len(d_ij)

        def dfs(start_i: int, start_j: int):
            queue = deque()
            queue.append((start_i, start_j))
            grid[start_i][start_j] = -1

            while queue:
                (cur_i, cur_j) = queue.popleft()

                for (d_i, d_j) in d_ij:
                    next_i = cur_i + d_i
                    next_j = cur_j + d_j

                    if (next_i < 0) or (next_j < 0) or (next_i >= row_size) or (next_j >= col_size):
                        continue
                    if grid[next_i][next_j] == '1':
                        queue.append((next_i, next_j))
                        grid[next_i][next_j] = -1

        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == '1':
                    island_cnt += 1
                    dfs(i, j)
                else:
                    continue
        
        return island_cnt
    
    """
    Keyword: MST, Kruskal, Find Union
    Space: O(N^2)
    Time: O(NlogN)
    """
    def find_union_solution(self, grid: List[List[str]]) -> int:
        # 그래프 탐색 대신, 집합 find-union을 이용하는 흐름.

        row_size = len(grid)
        col_size = len(grid[0])

        island_cnt = sum(grid[i][j] == '1' for i in range(row_size) for j in range(col_size))
        roots = [idx for idx in range(row_size * col_size)]
        
        def find(idx: int):
            if roots[idx] == idx:
                return idx
            else:
                return find(roots[idx])

        def union(idx1: int, idx2: int):
            root1, root2 = find(idx1), find(idx2)
            if root1 == root2:
                return
            
            nonlocal island_cnt
            island_cnt -= 1
            roots[root2] = root1

        for i in range(row_size):
            for j in range(col_size):
                if grid[i][j] == '0':
                    continue
                
                idx = i*col_size + j
                if (j < col_size-1) and (grid[i][j+1] == '1'):
                    union(idx, idx+1)
                if (i < row_size-1) and (grid[i+1][j] == '1'):
                    union(idx, idx+col_size)
        
        return island_cnt
