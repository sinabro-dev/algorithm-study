"""
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description/

You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
Return the maximum number of events you can attend.

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
"""
class Solution:
    """
    Keyword: Sort, Priority Queue
    Space: O(n)
    Time: O(nlogn)
    """
    def maxEvents(self, events: List[List[int]]) -> int:
        # events를 1차적으로 start 기준으로 내림차순 정렬 후 동일한 경우 end 기준으로 내림차순 정렬
        # 여기서 내림차순으로 하는 이유는 나중에 events.pop() 형태로 진행할 거이기 때문에
        # 오름차순이 아닌 내림차순으로 정렬
        # 이후 힙에 각 event의 end를 삽입하여 나열해두고
        # 오직 하나만 참석으로 인정하고 나머지 요소들은 단순히 무시한다
        
        import heapq
        from collections import defaultdict

        events.sort(key=lambda arr: (-arr[0], -arr[1]))
        heap = list()
        cnt = 0
        day = 0

        while events or heap:
            if not heap:
                day = events[-1][0]
            
            while events and events[-1][0] <= day:
                heapq.heappush(heap, events.pop()[1])
            
            heapq.heappop(heap)
            cnt += 1

            while heap and heap[0] <= day:
                heapq.heappop(heap)

            day += 1
        
        return cnt
