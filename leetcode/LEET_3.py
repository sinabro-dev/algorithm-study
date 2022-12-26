"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without repeating characters.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    
    """
    Keyword: Hash Map, Sliding Window
    Space: O(N)
    Time: O(N)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_len = 0
        max_len = 0
        start_pos = 0
        pos_map = dict()

        for cur_pos, char in enumerate(s):
            prev_pos = pos_map.get(char)
            pos_map[char] = cur_pos

            if prev_pos == None or prev_pos < start_pos:
                cur_len += 1
            else:
                max_len = max(cur_len, max_len)
                cur_len = cur_pos - prev_pos
                start_pos = prev_pos + 1

        if cur_len > max_len:
            max_len = cur_len

        return max_len
