"""
https://leetcode.com/problems/remove-k-digits/description/

Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
"""
class Solution:
    """
    Keyword: Monotonic Stack
    Space: O(n)
    Time: O(n)
    """
    def removeKdigits(self, num: str, k: int) -> str:
        # 모노토닉 스택을 이용하여 스택 top과 핸들링 중인 숫자 중 큰 수를 k번까지 제거하는 흐름
        
        stack = list()

        for cur in num:
            while (k > 0) and (stack) and (stack[-1] > cur):
                k -= 1
                stack.pop()
            stack.append(cur)
        
        while k > 0:
            k -= 1
            stack.pop()
        
        ret = ''.join(stack)
        while ret and ret[0] == '0':
            ret = ret[1:]
        
        return ret if ret else '0'
