"""
https://leetcode.com/problems/detonate-the-maximum-bombs/description/

You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.
The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.
Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

Input: bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
Output: 5
Explanation:
The best bomb to detonate is bomb 0 because:
- Bomb 0 detonates bombs 1 and 2. The red circle denotes the range of bomb 0.
- Bomb 2 detonates bomb 3. The blue circle denotes the range of bomb 2.
- Bomb 3 detonates bomb 4. The green circle denotes the range of bomb 3.
Thus all 5 bombs are detonated.
"""
class Solution:
    """
    Keyword: Graph, DFS
    Space: O(n^2)
    Time: O(n^2)
    """
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Bomb을 Node로, 연이어 터지는 다른 Bomb이 있는 경우 Edge로 그래프를 형성.
        # 이때 단순히 그래프 형성한다면 O(n^2) 소요되어 문제가 될 수 있지만,
        # 이 문제의 경우 n <= 100 이므로 딱히 이슈가 되지 않음.

        from collections import deque

        n = len(bombs)
        nodes = list()

        for x, y, r in bombs:
            nodes.append(Node(x, y, r))

        for i in range(n):
            cur = nodes[i]

            for j in range(n):
                if i == j:
                    continue

                node = nodes[j]
                distance = (cur.x - node.x)**2 + (cur.y - node.y)**2

                if distance > cur.r**2:
                    continue
                
                cur.add(j)
        
        def search(idx: int, visited: set, cnt: list) -> None:
            visited.add(idx)
            cnt[0] += 1

            for target in nodes[idx].adj:
                if target in visited:
                    continue
                
                search(target, visited, cnt)
        
        max_cnt = 0
        
        for i in range(n):
            cnt = [0]
            search(i, set(), cnt)
            
            max_cnt = max(cnt[0], max_cnt)
        
        return max_cnt


class Node:

    def __init__(self, x, y, r: int) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.adj = set()

    def add(self, elem: int) -> None:
        self.adj.add(elem)
