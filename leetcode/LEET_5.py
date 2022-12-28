"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""
class Solution:
    """
    Keyword: Dynamic Programming (DP)
    Space: O(N^2)
    Time: O(N^2)
    """
    def longestPalindrome(self, s: str) -> str:
        memo = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            memo[i][i] = True
        rng = (0, 0)

        sub_len = 2
        while sub_len <= len(s):
            start = 0
            while start < len(s) - (sub_len - 1):
                end = start + sub_len - 1

                if sub_len == 2 and s[start] == s[end]:
                    memo[start][end] = True
                    rng = (start, end) if end - start > rng[1] - rng[0] else rng
                elif s[start] == s[end] and memo[start+1][end-1]:
                    memo[start][end] = True
                    rng = (start, end) if end - start > rng[1] - rng[0] else rng
                
                start += 1
            sub_len += 1

        return s[rng[0] : rng[1]+1]
