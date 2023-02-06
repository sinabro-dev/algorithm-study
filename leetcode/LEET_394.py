"""
https://leetcode.com/problems/decode-string/description/

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""
class Solution:
    """
    Keyword: Recursion, Stack
    Space: O(n)
    Time: O(n)
    """
    def decodeString(self, s: str) -> str:
        numset = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        charset = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

        idx = 0
        ret = str()
        
        def decode() -> str:
            nonlocal idx
            cnt = 0

            while s[idx] in numset:
                cnt = int(s[idx]) + 10 * cnt
                idx += 1

            idx += 1
            sub = str()

            while s[idx] != ']':
                cur = s[idx]

                if cur in charset:
                    sub = ''.join([sub, cur])
                else:
                    sub = ''.join([sub, decode()])
                
                idx += 1
            
            return ''.join([sub for _ in range(cnt)])

        while idx < len(s):
            if s[idx] in numset:
                ret = ''.join([ret, decode()])
            else:
                ret = ''.join([ret, s[idx]])

            idx += 1
        
        return ret
