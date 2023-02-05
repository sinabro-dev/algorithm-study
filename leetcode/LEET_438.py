"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution:
    """
    Keyword: Hash, Sliding Window
    Space: O(1)
    Time: O(n)
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # `p`를 구성하는 문자 수를 나타내는 해시맵을 구성하고,
        # `s`를 훑으며 해시맵의 모든 요소 값이 0이 될 때를 찾는 흐름.

        if len(s) < len(p):
            return list()
        
        s_len = len(s)
        p_len = len(p)

        from collections import defaultdict
        
        cond_map = defaultdict(int)
        for char in list(p):
            cond_map[char] += 1
        
        for idx in range(p_len):
            char = s[idx]
            cond_map[char] -= 1
        
        ret = list()

        if all(val == 0 for val in cond_map.values()):
            ret.append(0)

        for idx in range(p_len, s_len):
            out_char = s[idx - p_len]
            cond_map[out_char] += 1

            in_char = s[idx]
            cond_map[in_char] -= 1
            
            if all(val == 0 for val in cond_map.values()):
                ret.append(idx - p_len + 1)
        
        return ret
