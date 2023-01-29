"""
https://leetcode.com/problems/word-search/description/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""
class Solution:
    """
    Keyword: Backtracking
    Space: O(mn)
    Time: O(mnl)
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_size = len(board)
        col_size = len(board[0])

        d_row = [0, 0, -1, 1]
        d_col = [-1, 1, 0, 0]

        def search(pos: int, ptr: int, visit: dict) -> bool:
            visit[pos] = True

            if ptr == len(word):
                return True

            for i in range(4):
                next_row = (pos // col_size) + d_row[i]
                next_col = (pos % col_size) + d_col[i]

                if not ((0 <= next_row < row_size) and (0 <= next_col < col_size)):
                    continue
                
                if board[next_row][next_col] != word[ptr]:
                    continue
                
                next_pos = next_row * col_size + next_col
                if visit.get(next_pos):
                    continue
                elif search(next_pos, ptr + 1, visit):
                    return True
            
            visit[pos] = False

            return False
        
        for i in range(row_size * col_size):
            row = i // col_size
            col = i % col_size

            if board[row][col] != word[0]:
                continue
            
            if len(word) == 1:
                return True
            elif search(i, 1, dict()):
                return True
        
        return False
