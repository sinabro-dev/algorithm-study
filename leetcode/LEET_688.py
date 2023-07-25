"""
https://leetcode.com/problems/knight-probability-in-chessboard/description/

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
The knight continues moving until it has made exactly k moves or has moved off the chessboard.
Return the probability that the knight remains on the board after it has stopped moving.

Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(n^2)
    Time: O(n^2 * k)
    """
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # knight가 움직일 수 있는 곳들에 대해 DFS로 훑으며 보드에서 떨어졌는지 아닌지 확인 후
        # 계속 이동하다가 k번째 움직임을 마쳤으면 확률 계산
        # ------------------------------------------------------------------------------
        # 다만 메모리 제한에 걸리기 때문에 다이나믹 프로그래밍을 이용해서
        # 메모이제이션도 함께 활용

        memo = [[0.0]*n for _ in range(n)]
        memo[row][column] = 1.0

        for _ in range(k):
            next_memo = [[0.0]*n for _ in range(n)]

            for r in range(n):
                for c in range(n):
                    for dr, dc in [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]:
                        next_r = r+dr
                        next_c = c+dc

                        if not (0 <= next_r < n):
                            continue
                        if not (0 <= next_c < n):
                            continue
                        
                        next_memo[r][c] += memo[next_r][next_c] / 8.0
            
            memo = next_memo

        prob = 0.0
        for r in range(n):
            for c in range(n):
                prob += memo[r][c]
        
        return prob
