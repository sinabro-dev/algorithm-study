"""
https://leetcode.com/problems/unique-paths/description/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
class Solution:
    """
    Keyword: Dynamic Programming (DP), Combinations
    Space: O(1)
    Time: O(M+N)
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # 먼저 떠오른 생각은, 점화식 형태로 이전 결과를 이용하는 방식.
        # p(i, j) = p(i-1, j) + p(i, j-1)
        # 다른 생각은, 각각의 경로는 결국 오른쪽 이동과 아래쪽 이동들이 나열된
        # 조합이기 때문에 조합의 경우의 수를 구하는 방식.
        # 예를 들어 (m, n) = (3, 7) 이라면, 오른쪽 이동 6번과 아래쪽 이동 2번으로
        # 이뤄져야 하기 때문에, 8! / (6! * 2!) = 28 이다.

        def factorial(n: int) -> int:
            ret = 1
            for num in range(2, n+1):
                ret *= num
            return ret
        
        all_cases = factorial(m-1 + n-1)
        group_cases = factorial(m-1) * factorial(n-1)

        return int(all_cases / group_cases)
