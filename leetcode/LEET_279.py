"""
https://leetcode.com/problems/perfect-squares/description/

Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(n)
    Time: O(n)
    """
    def numSquares(self, n: int) -> int:
        memo = [-1 for _ in range(n+1)]
        memo[0] = 0
        memo[1] = 1

        def calculate(k: int) -> int:
            if memo[k] >= 0: return memo[k]

            val = 10**4
            max_root = int(math.sqrt(k))

            for root in reversed(range(1, max_root+1)):
                remain = k - root**2
                prev = calculate(remain)
                val = min(val, 1+prev)
            
            memo[k] = val
            return val

        return calculate(n)
