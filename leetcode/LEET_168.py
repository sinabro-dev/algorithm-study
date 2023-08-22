"""
https://leetcode.com/problems/excel-sheet-column-title/description/

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Input: columnNumber = 701
Output: "ZY" 
"""
class Solution:
    """
    Keyword: String, Math
    Space: O(1)
    Time: O(n)
    """
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ''

        while columnNumber > 0:
            cur = columnNumber % 26
            if cur == 0: cur = 26
            
            char = chr(64 + cur)
            ret = ''.join([char, ret])

            columnNumber = columnNumber // 26
            if cur == 26: columnNumber -= 1
        
        return ret
