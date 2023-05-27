"""
https://leetcode.com/problems/non-overlapping-intervals/description/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""
class Solution:
    """
    Keyword: Greedy
    Space: O(n)
    Time: O(nlogn)
    """
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 유의할 점은 Non-Overlapping 간격을 만드는 것이지, Continued 할 필요는 없다는 것임.
        # 풀이를 위해 특정 구간에서 이를 이루는 세부 구간의 수를 알아야 함.
        # 이를 위해 다이나믹 프로그래밍 / 메모이제이션해야 하지만,
        # 그리디 관점에서 구간들을 정렬하면 구간 정보를 몰라도 풀이 가능함.

        pointer = float('-inf')
        cnt = 0

        for start, end in sorted(intervals, key=lambda arr: arr[1]):
            if start >= pointer:
                pointer = end
            else:
                cnt += 1

        return cnt
