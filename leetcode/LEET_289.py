"""
https://leetcode.com/problems/game-of-life/description/

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
"""
class Solution:
    """
    Keyword: Simulation
    Space: O(1)
    Time: O(nm)
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        # in-place 문제 해결을 위해 board[i][j] 값의 종류를 확장
        # 0->0: 0
        # 0->1: 2
        # 1->0: -1
        # 1->1: 1

        n, m = len(board), len(board[0])

        def check(r, c: int) -> (int, int):
            live, dead = 0, 0

            if (r-1 >= 0) and (c-1 >= 0):
                if board[r-1][c-1] == 0 or board[r-1][c-1] == 2:
                    dead += 1
                elif board[r-1][c-1] == -1 or board[r-1][c-1] == 1:
                    live += 1
            if (r-1 >= 0):
                if board[r-1][c] == 0 or board[r-1][c] == 2:
                    dead += 1
                elif board[r-1][c] == -1 or board[r-1][c] == 1:
                    live += 1
            if (r-1 >= 0) and (c+1 < m):
                if board[r-1][c+1] == 0 or board[r-1][c+1] == 2:
                    dead += 1
                elif board[r-1][c+1] == -1 or board[r-1][c+1] == 1:
                    live += 1
            if (c+1 < m):
                if board[r][c+1] == 0 or board[r][c+1] == 2:
                    dead += 1
                elif board[r][c+1] == -1 or board[r][c+1] == 1:
                    live += 1
            if (r+1 < n) and (c+1 < m):
                if board[r+1][c+1] == 0 or board[r+1][c+1] == 2:
                    dead += 1
                elif board[r+1][c+1] == -1 or board[r+1][c+1] == 1:
                    live += 1
            if (r+1 < n):
                if board[r+1][c] == 0 or board[r+1][c] == 2:
                    dead += 1
                elif board[r+1][c] == -1 or board[r+1][c] == 1:
                    live += 1
            if (r+1 < n) and (c-1 >= 0):
                if board[r+1][c-1] == 0 or board[r+1][c-1] == 2:
                    dead += 1
                elif board[r+1][c-1] == -1 or board[r+1][c-1] == 1:
                    live += 1
            if (c-1 >= 0):
                if board[r][c-1] == 0 or board[r][c-1] == 2:
                    dead += 1
                elif board[r][c-1] == -1 or board[r][c-1] == 1:
                    live += 1
            
            return (live, dead)
        
        for r in range(n):
            for c in range(m):
                live, dead = check(r, c)
            
                if board[r][c] == 0:
                    if live == 3:
                        board[r][c] = 2
                else:
                    if not 2 <= live <= 3:
                        board[r][c] = -1

        for r in range(n):
            for c in range(m):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == -1:
                    board[r][c] = 0
