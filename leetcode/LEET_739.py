"""
https://leetcode.com/problems/daily-temperatures/description/

Given an array of integers temperatures represents the daily temperatures, return an array answer such that
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""
class Solution:
    """
    Keyword: Heap(Priority Queue)
    Space: O(n)
    Time: O(n log n)
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # `temperatures` 리스트를 훑으며 각 요소에 대해 최소힙 내의 첫 요소가 더 작은 값을 갖는 경우
        # `answer` 리스트를 업데이트해준 후, 현 요소를 최소힙에 넣음을 반복
        
        import heapq

        answer = [0 for _ in range(len(temperatures))]
        queue = list()

        for day in range(len(temperatures)):
            temp = temperatures[day]

            while queue:
                (prev_temp, prev_day) = queue[0]
                if prev_temp >= temp:
                    break
                
                heapq.heappop(queue)
                answer[prev_day] = day - prev_day

            heapq.heappush(queue, (temp, day))
        
        return answer
