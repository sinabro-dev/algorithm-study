"""
https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
class Solution:
    """
    Keyword: Bit Masking
    Space: O(N)
    Time: O(2^N)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = list()
        size = len(nums)

        for mask in range(1 << size):
            subset = list()
            for idx in range(size):
                if (mask >> idx) & 0x1:
                    subset.append(nums[idx])
            subsets.append(subset)
        
        return subsets
