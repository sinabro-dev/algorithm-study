"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
"""
class Solution:
    """
    Keyword: Two Pointers, Dynamic Programming, Stack
    Space: O(n)
    Time: O(n)
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 특정 높이의 사각형이 포함된 최대 넓이의 왼쪽 x좌표와 오른쪽 x좌표를 구하고
        # 0부터 가장 높은 높이까지 각 높이일 때 가장 넓은 넓이를 비교해가며 최댓값을 찾음

        left = [-1] * len(heights)
        right = [len(heights)] * len(heights)

        for cur in range(1, len(heights)):
            before = cur-1

            while (before >= 0) and (heights[before] >= heights[cur]):
                before = left[before]
            
            left[cur] = before
        
        for cur in range(len(heights)-2, -1, -1):
            after = cur+1

            while (after < len(heights)) and (heights[after] >= heights[cur]):
                after = right[after]
            
            right[cur] = after
        
        area = 0
        for idx, height in enumerate(heights):
            area = max(area, height * (right[idx]-left[idx]-1))
        
        return area
