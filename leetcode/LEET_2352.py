"""
https://leetcode.com/problems/equal-row-and-column-pairs/description/

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""
class Solution:
    """
    Keyword: Hash Table, Simulation
    Space: O(n^2)
    Time: O(n^3)
    """
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict

        n = len(grid)
        cnt_map = defaultdict(int)
        ret = 0

        for i in range(n):
            row = grid[i]
            cnt_map[tuple(row)] += 1

        for j in range(n):
            col = [grid[i][j] for i in range(n)]
            ret += cnt_map[tuple(col)]

        return ret
