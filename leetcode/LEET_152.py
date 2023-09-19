"""
https://leetcode.com/problems/maximum-product-subarray/description/

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
- 1 <= nums.length <= 2 * 104
- 10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    """
    Keyword: Two Pointers
    Space: O(1)
    Time: O(n)
    """
    def maxProduct(self, nums: List[int]) -> int:
        # 신경써야하는 요소는 음수인 수를 만났을 때
        # 위와 같은 수를 만나게되면 기존 product 최댓값이 최솟값이 되고
        # 기존 product 최솟값이 최댓값이 됨
        # 이 때문에 product 최댓값과 최솟값을 모두 계산하며 모든 요소를 훑음

        n = len(nums)
        ans = nums[0]
        max_val, min_val = nums[0], nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                max_val, min_val = min_val, max_val
            
            max_val = max(nums[i], max_val*nums[i])
            min_val = min(nums[i], min_val*nums[i])

            ans = max(ans, max_val)
        
        return ans
