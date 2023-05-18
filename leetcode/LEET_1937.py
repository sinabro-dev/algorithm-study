"""
https://leetcode.com/problems/maximum-number-of-points-with-cost/description/

You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
Return the maximum number of points you can achieve.

Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
"""
class Solution:
    """
    Keyword: Dynamic Programming (DP)
    Space: O(n)
    Time: O(mn)
    """
    def maxPoints(self, points: List[List[int]]) -> int:
        # 가장 나이브한 풀이는 각 행마다 다음 행의 셀 하나씩 훑어보며
        # 최댓값을 갖는 걸 찾아내는 방법으로 m * n^2 시간이 소요.
        # 이를 개선하려면, 어느 한 행의 셀에서의 최댓값을 구할 때
        # 이전 행의 셀들을 훑지 않고 바로 구할 수 있어야 함.
        # 왼쪽에서 오른쪽으로 한번 훑으면서 최댓값을,
        # 오른쪽에서 왼쪽으로 한번 훑으면서 또 다른 최댓값을 구한 후
        # 그 둘을 비교하여 최종 최댓값을 구함.

        rows, cols = len(points), len(points[0])

        if rows == 1:
            return max(points[0])
        if cols == 1:
            return sum(sum(p) for p in points)
        
        def left_val(prev: list) -> list:
            left = [0]*cols
            left[0] = prev[0]

            for c in range(1, cols):
                left[c] = max(left[c-1]-1, prev[c])
            
            return left
        
        def right_val(prev: list) -> list:
            right = [0]*cols
            right[-1] = prev[-1]

            for c in reversed(range(cols-1)):
                right[c] = max(right[c+1]-1, prev[c])
            
            return right

        prev = points[0]
        for r in range(rows-1):
            left, right, cur = left_val(prev), right_val(prev), [0]*cols
            for c in range(cols):
                cur[c] = points[r+1][c] + max(left[c], right[c])
            prev = cur[:]
        
        return max(prev)
