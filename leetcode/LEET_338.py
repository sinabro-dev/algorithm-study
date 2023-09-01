"""
https://leetcode.com/problems/counting-bits/description/?envType=daily-question&envId=2023-09-01

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
- 0 <= n <= 105

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
class Solution:
    """
    Keyword: Dynamic Programming, Bit Manipulation
    Space: O(n)
    Time: O(n)
    """
    def countBits(self, n: int) -> List[int]:
        # 0000000 0     0
        # 0000001 1     1
        # 0000010 2     1
        # 0000011 3     2
        # 0000100 4     1
        # 0000101 5     2
        # 0000110 6     2
        # 0000111 7     3
        # 0001000 8     1
        # 0001001 9     2
        # 0001010 10    2
        # 0001011 11    3
        # 0001100 12    2
        # 0001101 13    3
        # 0001110 14    3
        # 0001111 15    4
        # 0010000 16    1

        import math

        ret = [0 for _ in range(n+1)]
        for num in range(1, n+1):
            p = int(math.log2(num))
            q = num - int(math.pow(2, p))
            ret[num] = 1 + ret[q]
        
        return ret
