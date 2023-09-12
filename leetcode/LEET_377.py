"""
https://leetcode.com/problems/combination-sum-iv/description/?envType=daily-question&envId=2023-09-09

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The test cases are generated so that the answer can fit in a 32-bit integer.
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of nums are unique.
- 1 <= target <= 1000

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
"""
class Solution:
    """
    Keyword: Recursion, Dynamic Programming
    Space: O(n)
    Time: O(n*t)
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 먼저 재귀 형태로 구현 후 다이나믹 프로그래밍 이용하여 수정
        # 이후 함수 호출 형태 대신, botom-to-top 구조로 변경

        n = len(nums)
        memo = [0 for _ in range(target+1)]
        memo[0] = 1

        for cur in range(1, target+1):
            for num in nums:
                if cur-num < 0: continue
                memo[cur] += memo[cur-num]
        
        return memo[target]

        # memo = [-1 for _ in range(target+1)]
        
        # def check(cur: int) -> int:
        #     if cur > target:
        #         return 0
        #     if cur == target:
        #         return 1
        #     if memo[cur] != -1:
        #         return memo[cur]
            
        #     case = 0
        #     for num in nums:
        #         case += check(cur + num)
            
        #     memo[cur] = case
        #     return case
        
        # return check(0)
