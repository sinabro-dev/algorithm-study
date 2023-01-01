"""
https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
"""
class Solution:
    """
    Keyword: DFS
    Space: O(V)
    Time: O(V+E)
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from enum import Enum

        class Status(Enum):
            White = 1
            Gray = 2
            Black = 3

        class Node:
            def __init__(self, id: int):
                self.id = id
                self.next = list()
                self.status = Status.White
                self.discovery = -1
                self.finish = -1
        
        nodes = [Node(i) for i in range(numCourses)]

        for [adv, base] in prerequisites:
            nodes[base].next.append(adv)
        
        def visit(cur_id: int) -> bool:
            nonlocal tick
            tick += 1

            cur_node = nodes[cur_id]
            cur_node.status = Status.Gray
            cur_node.discovery = tick

            for next_id in cur_node.next:
                next_status = nodes[next_id].status
                is_acyclic = True

                if next_status == Status.White:
                    is_acyclic = visit(next_id)
                elif next_status == Status.Gray:
                    is_acyclic = False
                
                if not is_acyclic:
                    return False
            
            tick += 1

            cur_node.status = Status.Black
            cur_node.finish = tick

            return True

        tick = 0

        for i, node in enumerate(nodes):
            if node.status == Status.White:
                is_acyclic = visit(i)
                if not is_acyclic:
                    return False

        for node in nodes:
            if node.status != Status.Black:
                return False

        return True
