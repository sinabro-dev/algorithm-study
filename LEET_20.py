"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
"""
class Solution:
    """
    Keywords: Stack
    Space: O(N)
    Time: O(N)
    """
    def isValid(self, s: str) -> bool:
        stack = list()

        for char in list(s):
            if char in ['(', '[', '{']:
                stack.append(char)
                continue
            
            if len(stack) == 0:
                return False

            top = stack.pop()

            if char == ')' and top == '(':
                continue
            elif char == ']' and top == '[':
                continue
            elif char == '}' and top == '{':
                continue
            else:
                return False

        if len(stack) != 0:
            return False
        else:
            return True
