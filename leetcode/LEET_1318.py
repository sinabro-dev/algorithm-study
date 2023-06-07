"""
https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/

Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
"""
class Solution:
    """
    Keyword: Bit Manipulation
    Space: O(1)
    Time: O(n)
    """
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0

        while c != 0:
            la, lb, lc = a&1, b&1, c&1

            a >>= 1
            b >>= 1
            c >>= 1

            if la | lb == lc:
                continue
            
            if lc == 1:
                cnt += 1
            elif (la == 1) and (lb == 1):
                cnt += 2
            else:
                cnt += 1
        
        while a != 0:
            if a&1 == 1:
                cnt += 1
            a >>= 1
        
        while b != 0:
            if b&1 == 1:
                cnt += 1
            b >>= 1

        return cnt
