"""
https://leetcode.com/problems/unique-paths-ii/description/

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
- m == obstacleGrid.length
- n == obstacleGrid[i].length
- 1 <= m, n <= 100
- obstacleGrid[i][j] is 0 or 1
 
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(mn)
    Time: O(mn)
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 처음에는 DFS로 가능한 경로 모두 탐색하려 했으나 Time Limit Exceed
        # 따라서 다이나믹 프로그래밍으로 반복 작업을 잡으려 함
        # memo(i, j) = memo(i-1, j) + memo(i, j-1)

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[0 for _ in range(cols)] for _ in range(rows)]
        memo[0][0] = 1

        for r in range(rows):
            for c in range(cols):
                if r+1 < rows and obstacleGrid[r+1][c] == 0:
                    memo[r+1][c] += memo[r][c]
                if c+1 < cols and obstacleGrid[r][c+1] == 0:
                    memo[r][c+1] += memo[r][c]
        
        return memo[rows-1][cols-1]
