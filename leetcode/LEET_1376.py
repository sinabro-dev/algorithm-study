"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.
The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
Return the number of minutes needed to inform all the employees about the urgent news.

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
The tree structure of the employees in the company is shown.
"""
class Solution:
    """
    Keyword: Tree, DP (Dynamic Programming), DFS
    Space: O(n)
    Time: O(n)
    """
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        ret = 0

        costs = [-1 for _ in range(n)]
        costs[headID] = 0

        def cal_cost(employee: int) -> None:
            if costs[employee] != -1:
                return
            
            nonlocal ret
            boss = manager[employee]

            cal_cost(boss)
            cost = costs[boss] + informTime[boss]

            ret = max(ret, cost)
            
            costs[employee] = cost
        
        for id in range(n):
            cal_cost(id)
        
        return ret
