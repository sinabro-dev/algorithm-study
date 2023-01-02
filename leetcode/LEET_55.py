"""
https://leetcode.com/problems/jump-game/description/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""
class Solution:
    """
    Keyword: Greedy
    Space: O(1)
    Time: O(N)
    """
    def canJump(self, nums: List[int]) -> bool:
        # 뒤에서부터 역순으로, 해당 index에서 점프할 수 있는 index의
        # 목적지 도착 여부에 따라 현재 index의 여부를 결정.

        least_jump = 1
        reachable = True

        for cur_pos in reversed(range(0, len(nums) - 1)):
            cur_jump = nums[cur_pos]
            reachable = False

            if cur_jump >= least_jump:
                least_jump = 1
                reachable = True
            else:
                least_jump += 1
                reachable = False

        return reachable
