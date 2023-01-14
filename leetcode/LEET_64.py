"""
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""
class Solution:
    """
    Keyword: DP, Dijkstra
    Space: O(N^2)
    Time: O(N^2logN^2)
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 다익스트라 알고리즘 이용.

        row_cnt = len(grid)
        col_cnt = len(grid[0])

        queue = list()
        distances = [100 * 200 * 200] * row_cnt * col_cnt

        heapq.heappush(queue, (0, 0))
        distances[0] = grid[0][0]

        while queue:
            cost, pos = heapq.heappop(queue)
            if cost > distances[pos]:
                continue
            
            row = pos // col_cnt
            col = pos % col_cnt

            for (row_offset, col_offset) in [(1, 0), (0, 1)]:
                next_row = row + row_offset
                if next_row >= row_cnt:
                    continue

                next_col = col + col_offset
                if next_col >= col_cnt:
                    continue

                cur_distance = distances[pos]
                next_cost = grid[next_row][next_col]
                next_pos = next_row*col_cnt + next_col
                next_distance = distances[next_pos]

                if next_distance > cur_distance + next_cost:
                    distances[next_pos] = cur_distance + next_cost
                    heapq.heappush(queue, (cur_distance + next_cost, next_pos))

        dst = row_cnt*col_cnt - 1
        return distances[dst]
