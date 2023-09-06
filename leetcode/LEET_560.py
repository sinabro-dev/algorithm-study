"""
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
- 1 <= nums.length <= 2 * 104
- 1000 <= nums[i] <= 1000
- 107 <= k <= 107

Input: nums = [1,2,3], k = 3
Output: 2
"""
class Solution:
    """
    Keyword: Prefix Sum, Hash Table
    Space: O(n)
    Time: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 앞에서부터 훑으며 subarray 총합을 딕셔너리에 저장해놓고
        # 총합과 k 값의 차가 딕셔너리에 존재하면
        # 딕셔너리 value에 해당하는 만큼 가능한 것

        mapper = dict()
        mapper[0] = 1
        total, cnt = 0, 0

        for i in range(len(nums)):
            total += nums[i]

            if total - k in mapper:
                cnt += mapper[total-k]
            
            if total in mapper:
                mapper[total] += 1
            else:
                mapper[total] = 1
            
        return cnt
