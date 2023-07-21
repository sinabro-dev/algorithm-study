"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(n)
    Time: O(n^2)
    """
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # nums 요소들을 훑으며 이전 요소까지의 LIS 길이 중 최댓값을 찾아서
        # 그에 해당하는 요소 개수를 구한다
        # 즉 LIS 길이와 LIS 수를 기록해가며 끝까지 반복

        s_len = 0
        n = len(nums)
        memo, cnt = [1]*n, [1]*n

        for i in range(n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue

                if memo[i] == memo[j]+1:
                    cnt[i] += cnt[j]
                elif memo[i] < memo[j]+1:
                    memo[i] = memo[j]+1
                    cnt[i] = cnt[j]
                
            s_len = max(s_len, memo[i])

        s_cnt = 0
        for i in range(n):
            if memo[i] != s_len:
                continue
            s_cnt += cnt[i]
        
        return s_cnt
