"""
https://leetcode.com/problems/n-th-tribonacci-number/description/

The Tribonacci sequence Tn is defined as follows:
- T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Input: n = 4
Output: 4
Explanation:
- T_3 = 0 + 1 + 1 = 2
- T_4 = 1 + 1 + 2 = 4
"""
class Solution:
    """
    Keyword: DP, Memoization
    Space: O(n)
    Time: O(n)
    """
    def tribonacci(self, n: int) -> int:
        val_map = dict()
        val_map[0] = 0
        val_map[1] = 1
        val_map[2] = 1

        def calculate(n: int) -> int:
            val = val_map.get(n)
            if val != None:
                return val
            
            val = calculate(n-1) + calculate(n-2) + calculate(n-3)
            val_map[n] = val

            return val
        
        return calculate(n)
