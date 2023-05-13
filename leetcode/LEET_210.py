"""
https://leetcode.com/problems/course-schedule-ii/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
"""
class Solution:
    """
    Keyword: Graph, DFS
    Space: O(n^2)
    Time: O(n)
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # hard_course->easy_course 구조의 그래프를 형성 후,
        # DFS 수행 및 각 노드의 방문 여부를 3가지 Color로 표시하며 가능 여부 결정

        nodes = [Node(i) for i in range(numCourses)]

        for req in prerequisites:
            advanced = nodes[req[0]]
            basic = nodes[req[1]]

            advanced.add(basic)
        
        order = list()
        
        def search(node: Node) -> bool:
            node.color = 0

            for req in node.reqs:
                if req.color > 0:
                    continue
                elif req.color == 0:
                    return False
                
                if not search(req):
                    return False

            node.color = 1
            order.append(node.id)
            return True

        for node in nodes:
            if node.color >= 0:
                continue

            if not search(node):
                return list()

        return order


class Node:
    def __init__(self, id: int):
        self.id = id
        self.reqs = list()
        self.color = -1
    
    def add(self, prerequsite):
        self.reqs.append(prerequsite)
