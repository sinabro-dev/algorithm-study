"""
https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

You are given an integer array nums and an array queries where queries[i] = [vali, indexi].
For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.
Return an integer array answer where answer[i] is the answer to the ith query.

Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
"""
class Solution:
    """
    Keyword: Simulation
    Space: O(1)
    Time: O(N)
    """
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for num in nums:
            if num % 2 != 0:
                continue
            even_sum += num
        
        ret = list()

        for query in queries:
            val, idx = query[0], query[1]

            if (nums[idx] % 2 != 0) and (val % 2 != 0):
                even_sum += (nums[idx] + val)
            elif (nums[idx] % 2 == 0) and (val % 2 == 0):
                even_sum += val
            elif (nums[idx] % 2 == 0) and (val % 2 != 0):
                even_sum -= nums[idx]

            ret.append(even_sum)
            nums[idx] += val

        return ret
