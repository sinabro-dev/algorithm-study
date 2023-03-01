"""
https://leetcode.com/problems/roman-to-integer/description/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
class Solution:
    """
    Keyword: Hash, Math
    Space: O(1)
    Time: O(n)
    """
    def romanToInt(self, s: str) -> int:
        num = 0

        for idx in range(len(s)):
            char = s[idx]

            if char == 'I':
                if (idx+1 < len(s)) and (s[idx+1] in {'V', 'X'}):
                    num -= 1
                else:
                    num += 1
            elif char == 'V':
                num += 5
            elif char == 'X':
                if (idx+1 < len(s)) and (s[idx+1] in {'L', 'C'}):
                    num -= 10
                else:
                    num += 10
            elif char == 'L':
                num += 50
            elif char == 'C':
                if (idx+1 < len(s)) and (s[idx+1] in {'D', 'M'}):
                    num -= 100
                else:
                    num += 100
            elif char == 'D':
                num += 500
            elif char == 'M':
                num += 1000
        
        return num
