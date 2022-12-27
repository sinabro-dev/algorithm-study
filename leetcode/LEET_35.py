"""
https://leetcode.com/problems/search-insert-position/description/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2
"""

class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(logN)
    """
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        if start == end:
            return 0 if target <= nums[start] else 1

        while True:
            mid = (start + end) // 2
            num = nums[mid]

            if num == target:
                return mid

            if num < target:
                start = mid + 1
            else:
                end = mid - 1

            if start > end:
                return start
