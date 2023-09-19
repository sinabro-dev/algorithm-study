"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/?envType=daily-question&envId=2023-09-18

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.
A row i is weaker than a row j if one of the following is true:
- The number of soldiers in row i is less than the number of soldiers in row j.
- Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
- m == mat.length
- n == mat[i].length
- 2 <= n, m <= 100
- 1 <= k <= m
- matrix[i][j] is either 0 or 1

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4]
"""
class Solution:
    """
    Keyword: Heap
    Space: O(n)
    Time: O(nlogn)
    """
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 최소힙으로 soldier 적은 row 순서대로 정렬 후
        # 같은 soldier 수인 row인 경우 앞선 row를 우선 반환

        from heapq import heappush, heappop

        m, n = len(mat), len(mat[0])
        heap = list()

        for r in range(m):
            cnt = 0
            for elem in mat[r]: cnt += elem

            heappush(heap, (cnt, r))
        
        ans = list()

        while len(ans) < k:
            soldier, i = heappop(heap)

            second_heap = list()
            heappush(second_heap, i)

            while heap and heap[0][0] == soldier:
                _, j = heappop(heap)
                heappush(second_heap, j)
            
            while second_heap:
                ans.append(heappop(second_heap))
        
        return ans[:k]
