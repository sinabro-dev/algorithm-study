"""
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(n)
    Time: O(n)
    """
    def rob(self, nums: List[int]) -> int:
        # approach using the following sequence
        # 1. find recursive relation
        # 2. recursive (top-down)
        # 3. recursive + memo (top-down)
        # 4. iterative + memo (bottom-up)
        # 5. iterative + N variabels (bottom-up)
        # 
        # [step 1] figure out recursive relation
        # robber has 2 options
        # a) rob current house i
        #    get "i-th money + rob(i-2)"
        # b) don't rob current house i
        #    get "rob(i-1)"
        # rob(i) = max( money[i]+rob(i-2), rob(i-1) )
        # 
        # [step 2] recursive (top-down)
        # def step2(i: int) -> int:
        #     if i < 0: return 0
        #     return max(nums[i]+step2(i-2), rob(i-1))
        # return step2(len(nums)-1)
        # 
        # [step 3] recursive + memo (top-down)
        # memo = [-1 for _ in range(len(nums)+1)]
        # def step3(i: int) -> int:
        #     if i < 0: return 0
        #     if memo[i] >= 0: return memo[i]
        #     val = max(nums[i]+step3(i-2), step3(i-1))
        #     memo[i] = val
        #     return val
        # return step3(len(nums)-1)
        # 
        # [step4] iterative + memo (bottom-up)
        memo = [-1 for _ in range(len(nums)+1)]
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            memo[i+1] = max(nums[i]+memo[i-1], memo[i])
        return memo[-1]
        # 
        # [step5] iterative + N variables (bottom-up)
        # prev1, prev2 = 0, 0
        # for num in nums:
        #     tmp = prev1
        #     prev1 = max(num+prev2, prev1)
        #     prev2 = tmp
        # return prev1
