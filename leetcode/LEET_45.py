"""
https://leetcode.com/problems/jump-game-ii/description/

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
- 0 <= j <= nums[i] and
- i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
class Solution:
    """
    Keyword: DP, Greedy
    Space: O(n)
    Time: O(n^2)
    """
    def jump(self, nums: List[int]) -> int:
        length = len(nums)

        chances = [10001 for _ in range(length)]
        chances[0] = 0

        for idx in range(length - 1):
            chance = chances[idx]
            num = nums[idx]
            
            if chance == 10001:
                continue
            if num == 0:
                continue
            
            for jump in range(1, num + 1):
                reach = idx + jump
                
                if reach >= length:
                    break

                if chance + 1 < chances[reach]:
                    chances[reach] = chance + 1
        
        return chances[length - 1]
            
