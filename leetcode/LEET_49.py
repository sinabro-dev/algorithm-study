"""
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
class Solution:
    """
    Keyword: Hash, Sort
    Space: O(N)
    Time: O(NlogN)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map = dict()
        groups = list()

        for origin_str in strs:
            sort_str = ''.join(sorted(origin_str))
            idx = group_map.get(sort_str)

            if idx == None:
                idx = len(groups)
                group_map[sort_str] = idx
                groups.append([origin_str])
            else:
                groups[idx].append(origin_str)

        return groups
