"""
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.
A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(n)
    Time: O(n)
    """
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # 각 요소를 훑으며 "요소값-difference" 값이 사전에 있었는지와
        # 있었다면 몇번째 수열이었는지 확인한다

        from collections import defaultdict

        mapper = defaultdict(int)
        longest = 1

        for cur in arr:
            prev = cur - difference
            if prev not in mapper:
                mapper[cur] = 1
                continue
            
            mapper[cur] = mapper[prev] + 1
            longest = max(longest, mapper[cur])
        
        return longest
