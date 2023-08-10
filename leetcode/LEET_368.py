"""
https://leetcode.com/problems/largest-divisible-subset/description/

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
"""
class Solution:
    """
    Keyword: Dynamic Programming, Sorting
    Space: O(n)
    Time: O(n^2)
    """
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 먼저 재귀 관계를 찾아보면, 각 요소를 훑으며
        # 1) 기준 요소가 현재 요소와 나누어떨어지는 경우 저장 후 다음 요소에 대해서도 재귀 호출
        # 2) 기준 요소가 현재 요소와 나누어떨어지지 않는 경우 단순히 다음 요소에 대해서 재귀 호출

        nums.sort(key=lambda x: x)
        memo = [-1 for _ in range(len(nums))]

        def figure_out(mod, idx: int, subset: list) -> list:
            if idx >= len(nums):
                return subset[:]
            
            ret = list()
            if (len(subset) > memo[idx]) and (nums[idx] % mod == 0):
                memo[idx] = len(subset)
                subset.append(nums[idx])
                ret = figure_out(nums[idx], idx+1, subset)
                subset.pop()
            
            tmp = figure_out(mod, idx+1, subset)
            if len(tmp) > len(ret):
                ret = tmp
            
            return ret

        return figure_out(1, 0, list())
