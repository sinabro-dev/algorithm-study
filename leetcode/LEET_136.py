"""
https://leetcode.com/problems/single-number/description/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Input: nums = [4,1,2,1,2]
Output: 4
"""
class Solution:
    """
    Keyword: Bit Manipulation
    Space: O(1)
    Time: O(n)
    """
    def singleNumber(self, nums: List[int]) -> int:
        # 숫자들을 훑으며 XOR 연산으로 중복되는 비트의 경우 0으로 바꿔준다
        
        ret = 0
        for num in nums:
            ret ^= num
        
        return ret
