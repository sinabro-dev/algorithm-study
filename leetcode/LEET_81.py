"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
"""
class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(log n)
    """
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums)-1
        while left < right:
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        while left > 0 and nums[left] == nums[left-1]:
            left -= 1
        
        pivot = left

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            r_mid = (mid + pivot) % len(nums)

            if nums[r_mid] < target:
                left = mid + 1
            elif nums[r_mid] > target:
                right = mid - 1
            else:
                return True

        return False
