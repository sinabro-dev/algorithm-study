"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.
- n == nums.length
- 1 <= n <= 5000
- 5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""
class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(logn)
    """
    def findMin(self, nums: List[int]) -> int:
        # 이분탐색을 이용하여 오름차순이 끊기는 위치 찾기

        n = len(nums)
        left, right = 0, n-1

        while left < right:
            mid = left + (right-left)//2

            if nums[left] < nums[right]:
                right = mid
            elif nums[left] < nums[mid]:
                left = mid+1
            else:
                right = mid
        
        if left < n-1 and nums[left] > nums[left+1]:
            left += 1
        
        return nums[left]
