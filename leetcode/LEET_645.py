"""
https://leetcode.com/problems/set-mismatch/description/

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
- 2 <= nums.length <= 104
- 1 <= nums[i] <= 104

Input: nums = [1,2,2,4]
Output: [2,3]
"""
class Solution:
    """
    Keyword: Hash
    Space: O(n)
    Time: O(n)
    """
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1, -1]

        exist = set()
        for num in nums:
            if num in exist:
                ans[0] = num
            exist.add(num)
        
        for i in range(1, n+1):
            if i not in exist:
                ans[1] = i
                break
        
        return ans
