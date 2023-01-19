"""
https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(log(M * N))
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log(M*N))으로 해결하려면, Row와 Col에 대해 바이너리 서치를 하면 될 듯.

        row, col = len(matrix), len(matrix[0])

        start, end = 0, row-1
        while start < end:
            mid = (start + end) // 2
            if target < matrix[mid][0]:
                end = mid - 1
            elif target > matrix[mid][0]:
                if target <= matrix[mid][col-1]:
                    start = end = mid
                else:
                    start = mid + 1
            else:
                return True

        sub_matrix = matrix[start]

        start, end = 0, col-1
        while start < end:
            mid = (start + end) // 2
            if sub_matrix[mid] > target:
                end = mid - 1
            elif sub_matrix[mid] < target:
                start = mid + 1
            else:
                return True

        if sub_matrix[start] == target:
            return True
        
        return False
