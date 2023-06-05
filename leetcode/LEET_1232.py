"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
"""
class Solution:
    """
    Keyword: Geometry
    Space: O(1)
    Time: O(n)
    """
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def cal_slope(p1, p2: (int, int)) -> float:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]

            if dx == 0:
                return float('inf')
            return dy / dx

        slope = cal_slope(coordinates[0], coordinates[1])

        for i in range(2, len(coordinates)):
            if slope != cal_slope(coordinates[i], coordinates[0]):
                return False

        return True
