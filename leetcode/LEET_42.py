"""
https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""
class Solution:
    """
    Keyword: Monotonic Stack
    Space: O(n)
    Time: O(n)
    """
    def trap(self, height: List[int]) -> int:
        # 가장 낮은 높이에서부터 높은 높이 순서로 접근하며
        # 각 높이에서 블록을 훑으며 슬라이딩 윈도우 마냥 물을 담을 수 있는 구간을 찾아낸다
        # --------------------------------------------------------------------------------
        # 위의 풀이면 n^2 수준의 시간이 소요되기 때문에 시간초과가 우려된다
        # 따라서 다른 풀이법인 모노토닉 스택을 이용한다
        # 기본적으로 내림차순으로 정렬되는 스택을 토대로,
        # 현재 높이가 스택의 top보다 큰 값이라면 top의 이전 높이와 현재 높이 중 작은 값이 물이 고이는 높이가 된다
        # 더불어 스택에는 블록 인덱스를 기록하므로 이때 고이는 물의 폭도 구할 수 있다
        # 이 과정을 거친 후 스택 요소를 한번 pop 한다
        # 이를 반복하여 스택이 비어있을 때까지 반복한다

        trap = 0
        stack = list()

        for idx in range(len(height)):
            while stack and height[idx] > height[stack[-1]]:
                top = stack[-1]
                stack.pop()

                if not stack:
                    break
                
                h = min(height[stack[-1]], height[idx]) - height[top]
                w = idx - stack[-1] - 1
                trap += h*w
            
            stack.append(idx)
        
        return trap
