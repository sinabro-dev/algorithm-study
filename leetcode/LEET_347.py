"""
https://leetcode.com/problems/top-k-frequent-elements/description/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
class Solution:
    """
    Keyword: Sort, Hash, Heap
    Space: O(n)
    Time: O(nlogn)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums 리스트의 요소들을 훑으며 각 수가 몇개 있는지 맵핑
        # 맵핑을 훑으며 힙에 저장
        # k만큼 힙에서 추출

        from collections import defaultdict
        import heapq

        cnt_map = defaultdict(int)
        for num in nums:
            cnt_map[num] += 1
        
        heap = list()
        for num, cnt in cnt_map.items():
            heapq.heappush(heap, (-cnt, num))
        
        answer = list()
        for _ in range(k):
            _, num = heapq.heappop(heap)
            answer.append(num)
        
        return answer
