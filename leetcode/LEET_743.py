"""
https://leetcode.com/problems/network-delay-time/description/

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
"""
class Solution:
    """
    Keyword: Dijkstra, Priority Queue
    Space: O(v)
    Time: O(ve)
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 다익스트라 알고리즘을 이용해서 최단 거리를 구함
        # 모든 노드를 훑지 못하는 경우에는 -1을 반환

        import heapq

        graph = [list() for _ in range(n+1)]
        for time in times:
            src, dst, weight = time[0], time[1], time[2]
            graph[src].append((dst, weight))
        
        max_cost = 10**4 + 1
        distance = [max_cost for _ in range(n+1)]
        distance[k] = 0

        visited = set()

        heap = list()
        for node in range(1, n+1):
            heapq.heappush(heap, (distance[node], node))

        while heap:
            _, src = heapq.heappop(heap)

            if src in visited:
                continue
            
            visited.add(src)

            for dst, weight in graph[src]:
                if distance[src] + weight < distance[dst]:
                    distance[dst] = distance[src] + weight
                    heapq.heappush(heap, (distance[src] + weight, dst))
        
        cost = 0
        for node in range(1, n+1):
            if distance[node] == max_cost:
                return -1
            cost = max(cost, distance[node])

        return cost
