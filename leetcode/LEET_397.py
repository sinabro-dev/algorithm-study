"""
https://leetcode.com/problems/integer-replacement/description/

Given a positive integer n, you can apply one of the following operations:
If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1 or 7 -> 6 -> 3 -> 2 -> 1
"""
class Solution:
    """
    Keyword: Dynamic Programming (DP)
    Space: O(n)
    Time: O(log n)
    """
    def integerReplacement(self, n: int) -> int:
        from collections import defaultdict

        op_map = defaultdict(int)
        op_map[1] = 0

        def do(n: int) -> int:
            if n in op_map:
                return op_map[n]
            
            if n % 2 == 0:
                op = 1 + do(n // 2)
            else:
                op = 1 + min(do(n + 1), do(n - 1))

            op_map[n] = op
            return op
            
        return do(n)
