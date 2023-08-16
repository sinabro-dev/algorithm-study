"""
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Input: nums = [1,3,4,2,2]
Output: 2
"""
class Solution:
    """
    Keyword: Binary Search, Bit Manipulation, Two Pointers
    Space: O(1)
    Time: O(nlogn)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        # 이진 탐색을 활용해 풀이
        # [1, n] 범위에서 한 개의 숫자만 2번이상 반복됨을 이용하여
        # 매 탐색마다 mid 값보다 작거나 같은 수의 개수를 구한 후
        # 그 개수가 mid 값보다 작거나 같다면 left를 업데이트하고
        # 그 개수가 mid 값보다 크다면 right를 업데이트 시킴
        # 최종적으로 left와 right가 같거나 역전되는 순간 값이 중복되는 숫자
        
        n = len(nums)
        left, right = 1, n-1

        while left < right:
            mid = left + (right - left) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        
        return left
