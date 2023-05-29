"""
https://leetcode.com/problems/find-all-good-indices/description/

You are given a 0-indexed integer array nums of size n and a positive integer k.
We call an index i in the range k <= i < n - k good if the following conditions are satisfied:
- The k elements that are just before the index i are in non-increasing order.
- The k elements that are just after the index i are in non-decreasing order.
Return an array of all good indices sorted in increasing order.

Input: nums = [2,1,1,1,3,4,1], k = 2
Output: [2,3]
Explanation: There are two good indices in the array:
- Index 2. The subarray [2,1] is in non-increasing order, and the subarray [1,3] is in non-decreasing order.
- Index 3. The subarray [1,1] is in non-increasing order, and the subarray [3,4] is in non-decreasing order.
Note that the index 4 is not good because [4,1] is not non-decreasing.
"""
class Solution:
    """
    Keyword: Prefix Sum
    Space: O(n)
    Time: O(n)
    """
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        left = [False] * n
        good = list()
        for i in range(n):
            if not good:
                good.append(nums[i])
                continue
            
            if len(good) >= k:
                left[i] = True
            
            if good[-1] >= nums[i]:
                good.append(nums[i])
            else:
                good = [nums[i]]
                
        
        right = [False] * n
        good = list()
        for i in reversed(range(n)):
            if not good:
                good.append(nums[i])
                continue

            if len(good) >= k:
                right[i] = True
            
            if good[-1] >= nums[i]:
                good.append(nums[i])
            else:
                good = [nums[i]]
        
        ret = list()
        for i in range(n):
            if left[i] and right[i]:
                ret.append(i)
        return ret
