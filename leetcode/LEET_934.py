"""
https://leetcode.com/problems/shortest-bridge/description/

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
"""
class Solution:
    """
    Keyword: DFS, BFS
    Space: O(n)
    Time: O(n)
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # 두 섬 중 한 섬에서 시작해서 BFS로 water인 셀들로 확장
        # 그러던 중 다른 한 섬을 만나면 그때가 가장 짧은 다리의 길이

        size = len(grid)
        queue = list()
        step = 0

        def start_pos() -> (int, int):
            for row in range(size):
                for col in range(size):
                    if grid[row][col] == 1:
                        return (row, col)
        
        def mark_island(row: int, col: int) -> None:
            grid[row][col] = -1
            queue.append((row, col))

            for next_row, next_col in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                if 0<=next_row<size and 0<=next_col<size and grid[next_row][next_col] == 1:
                    mark_island(next_row, next_col)        

        init_row, init_col = start_pos()
        mark_island(init_row, init_col)

        while queue:
            buf = list()

            for row, col in queue:
                for next_row, next_col in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                    if 0<=next_row<size and 0<=next_col<size:
                        if grid[next_row][next_col] == 1:
                            return step
                        elif grid[next_row][next_col] == 0:
                            grid[next_row][next_col] = -1
                            buf.append((next_row, next_col))
            
            queue = buf
            step += 1
