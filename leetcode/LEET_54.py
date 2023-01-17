"""
https://leetcode.com/problems/spiral-matrix/description/

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    """
    Keyword: Simulation
    Space: O(1)
    Time: O(N^2)
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_size = len(matrix)
        col_size = len(matrix[0])

        directions = [(0, 1), (1, 0), (0 ,-1), (-1, 0)]
        d_size = len(directions)

        def derive_direction(cur_d: int, cur_row: int, cur_col: int) -> int:
            next_row = cur_row + directions[cur_d][0]
            next_col = cur_col + directions[cur_d][1]

            if (not 0 <= next_row < row_size) or (not 0 <= next_col < col_size):
                return (cur_d + 1) % d_size
            
            if -100 <= matrix[next_row][next_col] <= 100:
                return cur_d
            
            return (cur_d + 1) % d_size
        
        ret = list()
        cnt = 0
        i, j, d = 0, 0, 0

        while cnt < row_size * col_size:
            ret.append(matrix[i][j])
            matrix[i][j] = 999
            cnt += 1

            d = derive_direction(d, i, j)
            i += directions[d][0]
            j += directions[d][1]
        
        return ret
