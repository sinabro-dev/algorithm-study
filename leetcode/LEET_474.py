"""
https://leetcode.com/problems/ones-and-zeroes/description/

You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.
- 1 <= strs.length <= 600
- 1 <= strs[i].length <= 100
- strs[i] consists only of digits '0' and '1'
- 1 <= m, n <= 100

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(mn)
    Time: O(len(strs))
    """
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 먼저 Recursive 관계를 찾고,

        # infos = list()
        # for str in strs:
        #     zero, one = 0, 0
        #     for c in str:
        #         if c == '0': zero += 1
        #         elif c == '1': one += 1
        #     infos.append((zero, one))
        
        # def do(idx, p, q: int) -> int:
        #     if idx >= len(strs) or (p <= 0 and q <= 0):
        #         return 0
            
        #     zero, one = infos[idx]
        #     if zero > p or one > q:
        #         return do(idx+1, p, q)
            
        #     include = 1 + do(idx+1, p-zero, q-one)
        #     exclude = do(idx+1, p, q)

        #     return max(include, exclude)
        
        # return do(0, m, n)

        # 이를 토대로 Iterative 관계로 변경

        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for str in strs:
            zero, one = 0, 0
            for c in str:
                if c == '0': zero += 1
                elif c == '1': one += 1
            
            for p in range(m, zero-1, -1):
                for q in range(n, one-1, -1):
                    memo[p][q] = max(memo[p][q], 1 + memo[p-zero][q-one])
        
        return memo[m][n]
