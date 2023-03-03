"""
https://leetcode.com/problems/add-binary/description/

Given two binary strings a and b, return their sum as a binary string.

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    """
    Keyword: Simulation, Bit Manipulation
    Space: O(1)
    Time: O(max(a_len, b_len))
    """
    def addBinary(self, a: str, b: str) -> str:
        binary = ''

        idx_a, idx_b = len(a)-1, len(b)-1
        carry = 0

        while idx_a >= 0 and idx_b >= 0:
            tmp = carry + int(a[idx_a]) + int(b[idx_b])

            carry = tmp // 2
            num = tmp % 2

            binary = ''.join([str(num), binary])
            idx_a -= 1
            idx_b -= 1

        while idx_a >= 0:
            tmp = carry + int(a[idx_a])

            carry = tmp // 2
            num = tmp % 2

            binary = ''.join([str(num), binary])
            idx_a -= 1

        while idx_b >= 0:
            tmp = carry + int(b[idx_b])

            carry = tmp // 2
            num = tmp % 2

            binary = ''.join([str(num), binary])
            idx_b -= 1
        
        if carry == 1:
            binary = ''.join(['1', binary])

        return binary
