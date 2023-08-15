"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""
class Solution:
    """
    Keyword: Priority Queue, Heap
    Space: O(k)
    Time: O(nk)
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 정렬 알고리즘을 사용하지 않고 풀이해야 하므로
        # 크기가 k인 최소힙을 이용하여 풀이
        
        from heapq import heappush, heappop

        heap = list()

        for i in range(len(nums)):
            if len(heap) < k:
                heappush(heap, nums[i])
                continue
            
            if nums[i] <= heap[0]:
                continue
            
            if nums[i] > heap[0]:
                heappush(heap, nums[i])
                heappop(heap)
                continue
        
        return heap[0]
