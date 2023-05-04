"""
https://leetcode.com/problems/combination-sum/description/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""
class Solution:
    """
    Keyword: Recursion, Backtracking
    Space: O(n)
    Time: O(n^2)
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 뚜렷한 최적화 방법이 떠오르지 않음
        # 가능한 경우들을 백트래킹으로 전부 훑으며 탐색

        cases = list()

        def track(case: [int], cur: int, remain: int) -> None:
            if remain < 0:
                return
            
            if remain == 0:
                cases.append(case)
                return
            
            for i in range(cur, len(candidates)):
                candidate = candidates[i]
                track(case+[candidate], i, remain-candidate)

        track(list(), 0, target)
        return cases
