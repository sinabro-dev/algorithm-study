"""
https://leetcode.com/problems/move-zeroes/submissions/874792061/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
class Solution:
    """
    Keyword: Two Pointers
    Space: O(1)
    Time: O(N)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        zero_idx = 0
        for cur_idx in range(len(nums)):
            if nums[cur_idx] != 0:
                nums[cur_idx], nums[zero_idx] = nums[zero_idx], nums[cur_idx]
                zero_idx += 1
