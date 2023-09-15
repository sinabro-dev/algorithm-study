"""
https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters 
You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(mn)
    Time: O(mn)
    """
    def minDistance(self, word1: str, word2: str) -> int:
        # 반복 작업이 매우 많을 것이므로 다이나믹 프로그래밍을 활용
        # 먼저 재귀 형태로 구현해보고
        # 재귀에서 메모이제이션을 추가해보고
        # 마지막으로 bottom-top 형태로 구현함

        n1, n2 = len(word1), len(word2)
        memo = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(n1+1):
            memo[i][0] = i
        for j in range(n2+1):
            memo[0][j] = j
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j], memo[i-1][j-1])
        
        return memo[n1][n2]

        # memo = [[-1 for _ in range(len(word2))] for _ in range(len(word1))]
        # def recurse_memo(i, j: int) -> int:
        #     if i >= len(word1):
        #         return len(word2) - j
        #     if j >= len(word2):
        #         return len(word1) - i
            
        #     if memo[i][j] != -1:
        #         return memo[i][j]
            
        #     if word1[i] == word2[j]:
        #         memo[i][j] = recurse_memo(i+1, j+1)
        #     else:
        #         insert = 1 + recurse_memo(i, j+1)
        #         delete = 1 + recurse_memo(i+1, j)
        #         replace = 1 + recurse_memo(i+1, j+1)
        #         memo[i][j] = min(insert, delete, replace)
        #     return memo[i][j]
        # return recurse_memo(0, 0)

        # def recurse(word1, word2: str) -> int:
        #     if not word1:
        #         return len(word2)
        #     if not word2:
        #         return len(word1)
            
        #     if word1[0] == word2[0]:
        #         return recurse(word1[1:], word2[1:])
            
        #     insert = 1 + recurse(word1, word2[1:])
        #     delete = 1 + recurse(word1[1:], word2)
        #     replace = 1 + recurse(word1[1:], word2[1:])
        #     return min(insert, delete, replace)
        # return recurse(word1, word2)
        
