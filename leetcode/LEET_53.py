"""
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(n)
    Time: O(n)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        # nums 요소들을 훑으면서 각 index 이후의 값들에 대한
        # 최대 합을 memoization하여 문제를 푸는 흐름.

        memo = [0 for _ in range(len(nums))]
        memo[-1] = nums[-1]

        max_sum = nums[-1]

        for idx in reversed(range(len(nums)-1)):
            if memo[idx+1] < 0:
                memo[idx] = nums[idx]
            else:
                memo[idx] = nums[idx] + memo[idx+1]
            
            max_sum = max(max_sum, memo[idx])
        
        return max_sum
