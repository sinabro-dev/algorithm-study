"""
https://leetcode.com/problems/minimum-speed-to-arrive-on-time/description/

You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.
Each train can only depart at an integer hour, so you may need to wait in between each train ride.
- For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.
Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

Input: dist = [1,3,2], hour = 2.7
Output: 3
Explanation: At speed 3:
- The first train ride takes 1/3 = 0.33333 hours.
- Since we are not at an integer hour, we wait until the 1 hour mark to depart. The second train ride takes 3/3 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 2 hour mark. The third train takes 2/3 = 0.66667 hours.
- You will arrive at the 2.66667 hour mark.
"""
class Solution:
    """
    Keyword: Binary Search
    Space: O(1)
    Time: O(log n)
    """
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # 최대한 빠르게 움직였을 때의 속도에서 시작해서
        # 하나씩 속도를 낮춰가며 도착 가능할 때까지 반복 후
        # 최소 속도를 찾아야 함
        # 이때 최대 속도는 dist 요소 사이의 대기 시간이 각 1시간인 점을 고려하여,
        # 걸린 시간을 hour - 1 * (len(dist)-1) 으로 하고, 이동 거리를 sum(dist) 로 하여
        # 구할 수 있음
        # 또한 단순히 최대 속도에서 하나씩 속도를 낮춰가며 반복하면 시간 초과가 날 수 있으므로
        # 이진 탐색을 활용하여 속도를 찾아야 함

        n = len(dist)

        if n == 1:
            speed = math.ceil(dist[-1] / hour)
            if (speed-1)*hour >= dist[-1]:
                return speed-1
            else:
                speed
        if n-1 >= hour:
            return -1
        
        total_distance = sum(dist)
        min_hour = hour - (n-1)
        max_speed = math.ceil(total_distance / min_hour)

        start, end = 1, max_speed
        while start <= end:
            mid = (start + end) // 2

            time = 0
            for idx in range(n-1):
                time += math.ceil(dist[idx] / mid)
            time += dist[-1] / mid
        
            if time <= hour:
                end = mid - 1
            else:
                start = mid + 1
        
        return start
