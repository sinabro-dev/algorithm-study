"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/?envType=daily-question&envId=2023-09-20

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104
- 1 <= x <= 109

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
"""
class Solution:
    """
    Keyword: Prefix Sum, Sliding Window
    Space: O(1)
    Time: O(n)
    """
    def minOperations(self, nums: List[int], x: int) -> int:
        # nums 리스트 요소의 총합을 sum이라 하면
        # 이 문제는 sum-x를 총합으로 갖는 max length subarray를 찾는 것으로 볼 수 있음

        n = len(nums)

        target = 0
        for num in nums:
            target += num
        target -= x
    
        if target == 0:
            return n

        cnt = 0
        total = 0
        left, right = 0, 0

        for right in range(n):
            total += nums[right]

            while left <= right and total > target:
                total -= nums[left]
                left += 1
            
            if total == target:
                cnt = max(cnt, right-left+1)
        
        if cnt == 0:
            return -1
        else:
            return n - cnt
