"""
https://leetcode.com/problems/combinations/description/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
"""
class Solution:
    """
    Keyword: Backtracking
    Space: O(n^k)
    Time: O(n^k)
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Bit Masking만으로 풀이하기에는 복잡성이 높아지는 면이 있어서
        # 백트래킹으로 풀이

        cases = list()

        def do(case: list) -> None:
            if len(case) == k:
                cases.append(case)
                return
            
            minimum = case[-1] if case else 1
            for num in range(minimum, n+1):
                if num in case:
                    continue
                
                do(case+[num])
        
        do(list())
        
        return cases
