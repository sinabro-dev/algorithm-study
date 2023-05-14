"""
https://leetcode.com/problems/largest-number/description/

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Input: nums = [3,30,34,5,9]
Output: "9534330"
"""
class Solution:
    """
    Keyword: Sorting
    Space: O(n)
    Time: O(nlogn)
    """
    def largestNumber(self, nums: List[int]) -> str:
        # 기본적으로 Heap Sort를 이용하여 풀이
        # 다만 문제에서 요구하는 특수 비교 연산이 있으므로,
        # 커스텀 Comparator를 정의해야 함
        # 또한 최대힙을 이용해야 하므로 Comparator는 실제 대소비교와
        # 반대되는 값을 반환해야 함

        import heapq

        heap = list()
        zeros = 0

        for num in nums:
            heapq.heappush(heap, Node(num))
            if num == 0:
                zeros += 1

        if zeros == len(nums):
            return '0'
        
        ret = ''

        while heap:
            node = heapq.heappop(heap)
            ret = ''.join([ret, str(node.val)])
        
        return ret


class Node:
    def __init__(self, val: int):
        self.val = val
    
    def __lt__(self, other) -> bool:
        val1, val2 = self.val, other.val
        len1, len2 = len(str(val1)), len(str(val2))

        num1 = val1 * (10**len2) + val2
        num2 = val2 * (10**len1) + val1

        return num1 >= num2
