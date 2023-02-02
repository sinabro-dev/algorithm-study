"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(log n)
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        find = -1
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                find = mid
                break
        
        if find == -1:
            return [-1, -1]

        ret = list()
        start = find
        end = find

        offset = 1
        while True:
            if (start >= offset) and (nums[start - offset] == target):
                offset *= 2
                continue
            
            offset //= 2
            start -= offset

            if offset > 1:
                offset = 1
                continue
        
            ret.append(start)
            break
        
        offset = 1
        while True:
            if (end + offset < len(nums)) and (nums[end + offset] == target):
                offset *= 2
                continue
            
            offset //=2
            end += offset

            if offset > 1:
                offset = 1
                continue
            
            ret.append(end)
            break

        return ret
