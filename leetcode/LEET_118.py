"""
https://leetcode.com/problems/pascals-triangle/description/

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(n^2)
    Time: O(n^2)
    """
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = list()

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        
        triangle.append([1])
        triangle.append([1, 1])

        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            
            triangle.append(row)
        
        return triangle
