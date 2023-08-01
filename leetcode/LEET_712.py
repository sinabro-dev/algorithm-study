"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
"""
class Solution:
    """
    Keyword: Dynamic Programming
    Space: O(nm)
    Time: O(nm)
    """
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # s1[i]와 s2[j]가 같은 경우, i와 j 모두 증가시키고 넘어가면 됨
        # s1[i]와 s2[j]가 다른 경우, s1[i]를 제거하는 것과 s2[j]를 제거하는 것 중 하나를 선택
        # s1과 s2의 각 문자에 대해 두 가지 경우 핸들링
        # 이때 반복 작업을 줄이기 위해 다이나믹 프로그래밍 활용

        n1, n2 = len(s1), len(s2)
        memo = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(1, n1+1):
            memo[i][0] = memo[i-1][0] + ord(s1[i-1])
        
        for j in range(1, n2+1):
            memo[0][j] = memo[0][j-1] + ord(s2[j-1])
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if s1[i-1] == s2[j-1]:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    memo[i][j] = min(memo[i-1][j]+ord(s1[i-1]), memo[i][j-1]+ord(s2[j-1]))

        return memo[n1][n2]
