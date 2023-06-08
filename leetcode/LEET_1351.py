"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
"""
class Solution:
    """
    Keyword: Binary Search, Matrix
    Space: O(m)
    Time: O(m+n)
    """
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def find_point(i, prev: int) -> int:
            row = grid[i]
            for j in range(prev, n):
                if row[j] < 0:
                    return j
            return -1
        
        cnt = 0
        prev = 0

        for i in reversed(range(m)):
            j = find_point(i, prev)
            if j == -1:
                return cnt
            
            cnt += (n - j)
            prev = j
        
        return cnt
