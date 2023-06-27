"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""
class Solution:
    """
    Keyword: Priority Queue, Heap
    Space: O(k)
    Time: O(klogk)
    """
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq

        pairs = list()
        heap = list()
        visited = set()
        
        heapq.heappush(heap, (nums1[0]+nums2[0], (0, 0)))
        visited.add((0, 0))

        while heap:
            _, (i, j) = heapq.heappop(heap)
            
            pairs.append([nums1[i], nums2[j]])
            if len(pairs) == k:
                break

            if (i+1 < len(nums1)) and ((i+1, j) not in visited):
                heapq.heappush(heap, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if (j+1 < len(nums2)) and ((i, j+1) not in visited):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
        
        return pairs
