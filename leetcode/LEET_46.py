"""
https://leetcode.com/problems/permutations/description/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution:
    """
    Keyword: Backtracking
    Space: O(n)
    Time: O(n^2)
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        cases = list()

        nums_set = set(nums)

        def do(case: list) -> None:
            if len(case) == len(nums):
                cases.append(case)
                return
            
            tmp = nums_set.copy()
            for num in case:
                tmp.remove(num)
            
            for num in tmp:
                new = case.copy()
                new.append(num)
                do(new)
        
        do(list())

        return cases
