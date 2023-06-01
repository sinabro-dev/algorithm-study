"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
"""
class Solution:
    """
    Keyword: BFS
    Space: O(n^2)
    Time: O(n^2)
    """
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        
        n = len(grid)
        diff = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

        if grid[0][0] != 0:
            return -1
        if grid[n-1][n-1] != 0:
            return -1

        def next_move(row, col: int) -> [(int, int)]:
            moves = list()

            for d_row, d_col in diff:
                next_row = row + d_row
                next_col = col + d_col

                if not (0 <= next_row < n):
                    continue
                if not (0 <= next_col < n):
                    continue

                if grid[next_row][next_col] != 0:
                    continue
                
                moves.append((next_row, next_col))
            
            return moves
        
        queue = deque()
        queue.append((0, 0, 1))
        grid[0][0] = 1

        while queue:
            row, col, step = queue.popleft()
            
            if (row == n-1) and (col == n-1):
                return step

            for next_row, next_col in next_move(row, col):
                grid[next_row][next_col] = 1
                queue.append((next_row, next_col, step+1))

        return -1
