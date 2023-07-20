"""
https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

There is a function signFunc(x) that returns:
- 1 if x is positive.
- -1 if x is negative.
- 0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.
Return signFunc(product).

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
"""
class Solution:
    """
    Keyword: Math
    Space: O(1)
    Time: O(n)
    """
    def arraySign(self, nums: List[int]) -> int:
        ret = 1

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                ret *= -1
        
        return ret
