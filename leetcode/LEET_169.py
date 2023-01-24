"""
https://leetcode.com/problems/majority-element/description/

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    """
    Keyword: Hash, Divide and Conquer
    Space: O(1)
    Time: O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:
        # 단순 해시를 이용한 풀이는 O(N) 메모리가 필요하나,
        # 문제에서는 O(1)로 풀이를 권장.
        # 이에 맞게 무조건 하나의 원수는 과반수 이상 등장한다는 점을
        # 이용해 과반수 투표 알고리즘으로 접근.

        target = 0
        cnt = 0

        for num in nums:
            if cnt == 0:
                target = num
            
            if num == target:
                cnt += 1
            else:
                cnt -= 1
        
        return target
