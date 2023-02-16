"""
https://leetcode.com/problems/number-of-provinces/description/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""
class Solution:
    """
    Keyword: DFS, BFS, Union Find
    Space: O(n)
    Time: O(n^2)
    """
    def findCircleNum(self, connections: List[List[int]]) -> int:
        # 집합의 find-union 알고리즘으로 최종 집합 개수를 구하는 방식.
        # 이때 매번 각 도시의 최상단 값으로 업데이트하는 것이 아닌,
        # Bottom-Up으로 찾아가는 방법으로.

        city_num = len(connections)
        province_num = city_num
        parents = [city for city in range(city_num)]

        def find(city: int) -> int:
            if parents[city] == city:
                return city
            else:
                return find(parents[city])
        
        def union(city_a: int, city_b: int) -> None:
            nonlocal province_num
            parent_a, parent_b = find(city_a), find(city_b)

            if parent_a == parent_b:
                return
            
            parents[parent_b] = parent_a
            province_num -= 1
        
        for i in range(city_num):
            for j in range(i+1, city_num):
                if connections[i][j] == 0:
                    continue
                union(i, j)
        
        return province_num
