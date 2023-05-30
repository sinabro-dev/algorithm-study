"""
https://leetcode.com/problems/maximum-subsequence-score/description/

You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.
For chosen indices i0, i1, ..., ik - 1, your score is defined as:
- The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
- It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.
A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
"""
class Solution:
    """
    Keyword: Priority Queue, Heap, Sorting
    Space: O(n)
    Time: O(nlogn)
    """
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # 가장 나이브한 방법은 C(n, k) 경우를 모두 계산하며 최댓값을 찾는 것.
        # 이 방법은 뻔히 Time Limit이 될 것이기 때문에 시도 X.
        # 이 문제에서 'subsequence' 개념은 기존 요소들의 연속성을 고려하지 않음.
        # 즉, 임의로 요소들을 정렬해서 해결해도 됨.
        # 단, nums1와 nums2 사이의 인덱스 연관관계는 유지하며 정렬해야 함.
        # 내림차순으로 nums2 요소들을 훑으면, sum * min 계산 식에서 min에 해당하는 값은 더이상 변수가 아님.
        # 따라서 sum을 최대로 만드는 경우를 찾아서 이전의 계산 값과 비교하며 됨.
        # 이를 위해 최소힙을 활용.
        
        import heapq

        arr = list()
        for i in range(len(nums1)):
            arr.append((nums1[i], nums2[i]))
        pairs = sorted(arr, key=lambda pair: pair[1], reverse=True)
        
        heap = list()
        total = 0
        score = 0

        for num1, num2 in pairs:
            if len(heap) < k:
                heapq.heappush(heap, num1)
                total += num1
                score = total*num2
                continue
            
            top = heapq.heappop(heap)
            heapq.heappush(heap, num1)

            total -= top
            total += num1
            score = max(score, total*num2)

        return score
