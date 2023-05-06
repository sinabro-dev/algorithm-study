"""
https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
class Solution:
    """
    Keyword: Math
    Space: O(1)
    Time: O(n^2)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        # clockwise rotate
        # first reverse up to down, then swap the symmetry 
        # 1 2 3     7 8 9     7 4 1
        # 4 5 6  => 4 5 6  => 8 5 2
        # 7 8 9     1 2 3     9 6 3

        for idx in range(len(matrix)//2):
            matrix[idx], matrix[-idx-1] = matrix[-idx-1], matrix[idx]

        for row in range(len(matrix)):
            for col in range(row+1, len(matrix[row])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


class StuckSolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def cur_case(row: int, col: int) -> int:
            # 0011
            # 0  1
            # 3  2
            # 3322
            if row < (len(matrix)//2):
                if col < (len(matrix)//2):
                    return 0
                else:
                    return 1
            else:
                if col < (len(matrix)//2):
                    return 3
                else:
                    return 2

        def next_pos(row: int, col: int, size: int) -> (int, int):
            start = len(matrix)//2 - size//2
            end = len(matrix)//2 + size//2 + size%2 - 1

            case = cur_case(row, col)

            for i in range(1, size):
                move = moves[case]

                if (row+move[0] < start) or (row+move[0] > end) or (col+move[1] < start) or (col+move[1] > end):
                    case = (case+1) % len(moves)
                    move = moves[case]
                
                row += move[0]
                col += move[1]
            
            return (row, col)

        size = len(matrix)
        row, col = 0, 0

        while size > 1:
            init_row, init_col = row, col
            
            for case in range(1, size):
                next_val = matrix[row][col]

                for i in range(4):
                    next_row, next_col = next_pos(row, col, size)

                    tmp_val = matrix[next_row][next_col]
                    matrix[next_row][next_col] = next_val
                    next_val = tmp_val

                    row, col = next_row, next_col
                
                col += 1
            
            row, col = init_row+1, init_col+1
            size -= 2
