"""
https://leetcode.com/problems/set-matrix-zeroes/description/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
class Solution:
    """
    Keyword: Hash, Matrix
    Space: O(m+n)
    Time: O(mn)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        row = 0
        col = 0

        while True:
            if col == len(matrix[0]):
                row += 1
                col = 0
            if row == len(matrix):
                break
            
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)
            
            col += 1

        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
