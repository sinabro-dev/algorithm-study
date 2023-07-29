"""
https://leetcode.com/problems/merge-intervals/description/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""
class Solution:
    """
    Keyword: Sorting
    Space: O(nlogn)
    Time: O(nlogn)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals 배열을 1차적으로 start를 기준으로, 2차적으로 end를 기준으로 오름차순 정렬을 한 후
        # 앞에서부터 겹치는 요소들을 합쳐가며 최종 답을 구함

        intervals.sort(key=lambda arr: (arr[0], arr[1]))
        intervals.append([10001, 10001])

        ret = list()

        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                ret.append([start, end])
                start = intervals[i][0]
            
            end = max(end, intervals[i][1])
        
        return ret
