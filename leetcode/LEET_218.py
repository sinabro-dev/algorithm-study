"""
https://leetcode.com/problems/the-skyline-problem/description/

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
- lefti is the x coordinate of the left edge of the ith building.
- righti is the x coordinate of the right edge of the ith building.
- heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
"""
class Solution:
    """
    Keyword: Divide and Conquer, Heap(Priority Queue), Segment Tree, Binary Indexed Tree
    Space: O(n)
    Time: O(n log n)
    """
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # key point 변경될 수 있는 상황은 아래와 같음.
        # 1. 더 높은 건물이 있는 경우
        # 2. 건물의 `right`-`left`에 다다르는 경우
        # 1번은 쉽게 처리 가능하지만, 2번의 경우 차순위의 건물 높이를 알고 있어야 함.
        # 이를 위해 개량한 우선순위 큐를 활용하는 흐름.

        import heapq

        pq = list()
        ret = list()
        key_left, key_right, key_height = -1, buildings[0][1], 0

        for building in buildings:
            left, right, height = building[0], building[1], building[2]
            
            while key_right < left:
                while len(pq) > 0:
                    if pq[0][2] > key_right:
                        break
                    heapq.heappop(pq)
                
                if len(pq) == 0:
                    key_left, key_right, key_height = key_right, left, 0
                else:
                    key_left, key_right, key_height = key_right, pq[0][2], -pq[0][0]

                ret.append([key_left, key_height])
            
            heapq.heappush(pq, (-height, left, right))
            
            if height < key_height:
                continue

            if height == key_height:
                key_right = right
                continue

            if left == key_left:
                key_left, key_right, key_height = left, right, height
                ret[-1] = [key_left, key_height]
                continue

            key_left, key_right, key_height = left, right, height
            ret.append([key_left, key_height])
            
        while len(pq) > 0:
            height, left, right = -pq[0][0], pq[0][1], pq[0][2]
            heapq.heappop(pq)

            if right <= key_right:
                continue
            
            if height == key_height:
                key_left, key_right = key_right, right
                continue

            key_left, key_right, key_height = key_right, right, height
            ret.append([key_left, key_height])
        
        ret.append([key_right, 0])

        return ret
