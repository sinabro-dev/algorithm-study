"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(log n)
    """
    def search(self, nums: List[int], target: int) -> int:
        # Case 1. [1,2,3,4] | Case 2. [3,4,1,2] | Case 3. [2,3,4,1]
        # pivot과 target을 순차적으로 이진 탐색을 통해 찾는 흐름.

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            rotated_mid = (mid + pivot) % len(nums)

            if nums[rotated_mid] < target:
                left = mid + 1
            elif nums[rotated_mid] > target:
                right = mid - 1
            else:
                return rotated_mid
        
        return -1
