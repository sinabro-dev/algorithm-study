"""
https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
class Solution:
    """
    Keyword: Two Pointers
    Space: O(N)
    Time: O(N)
    """
    def maxArea(self, height: List[int]) -> int:
        # Brute-Force 방식으로 접근하면 O(N^2) 소요.
        # Pruning으로 답이 될 수 없는 경우를 스킵하더라도 시간 소요 큼.
        # 먼저 리스트를 height 내림차순으로 정렬 후,
        # 해당 height를 갖는 x좌표들을 맵핑해놓고,
        # height 내림차순으로 반복해가며 왼쪽 끝과 오른쪽 끝을 최신화하며
        # 최대 넓이를 찾아가는 흐름.

        size = len(height)
        h_map = dict()

        for idx, h in enumerate(height):
            idxes = h_map.get(h)
            if idxes == None:
                h_map[h] = [idx, idx]
            else:
                idxes[1] = idx
                h_map[h] = idxes
            
        h_list = sorted(h_map.keys(), reverse=True)
        h_len = len(h_list)

        left = size - 1
        right = 0
        max_area = 0

        for k in range(h_len):
            h = h_list[k]
            if h == 0:
                continue
            elif (max_area // h + 1) >= size:
                break
            
            idxes = h_map[h]
            first = idxes[0]
            last = idxes[-1]

            left = first if first < left else left
            right = last if last > right else right
            w = right - left
            
            cur_area = w * h
            max_area = cur_area if cur_area > max_area else max_area

        return max_area
