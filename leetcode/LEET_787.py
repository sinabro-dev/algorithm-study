"""
https://leetcode.com/problems/cheapest-flights-within-k-stops/description/

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
"""
class Solution:
    """
    Keyword: DP(Dynamic Programming), BFS, Heap(Priority Queue), Shortest Path
    Space: O(v + e)
    Time: O(e log v)
    """
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Stage 1. from -> (price, to) 꼴 형태로 데이터 가공
        # Stage 2. BFS로 src -> dst 경로 길이의 최솟값이 `k+1` 보다 작거나 같은지 검증.
        # Stage 3-1. 다익스트라 알고리즘으로 최단 거리 탐색
        # Stage 3-2. 단 한번 탐색한 노드도 다시 탐색할 수 있게 해서 k번째 최단 거리 탐색하도록

        import heapq
        from collections import defaultdict, deque

        adjacents = [list() for _ in range(n)]

        for flight in flights:
            depart, arrive, price = flight[0], flight[1], flight[2]
            adjacents[depart].append((price, arrive))
        
        min_path_len = defaultdict(int)

        searchings = deque()
        searchings.append((src, 1))

        while searchings:
            cur, num = searchings.pop()
            
            for (_, to) in adjacents[cur]:
                if (not to in min_path_len) or (num + 1 < min_path_len[to]):
                    min_path_len[to] = num + 1
                    searchings.append((to, num + 1))
        
        if not dst in min_path_len:
            return -1
        if min_path_len[dst] > k + 2:
            return -1

        flyings = list()
        heapq.heappush(flyings, (0, src, 1))

        while flyings:
            cost, depart, passes = heapq.heappop(flyings)

            if (depart == dst) and (passes <= k + 2):
                return cost
            
            for (price, arrive) in adjacents[depart]:
                heapq.heappush(flyings, (cost + price, arrive, passes + 1))
        
        return 0
