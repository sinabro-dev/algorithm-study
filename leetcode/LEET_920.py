"""
https://leetcode.com/problems/number-of-music-playlists/description/

Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:
- Every song is played at least once.
- A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
"""
class Solution:
    """
    Keyword: Dynamic Programming, Combination
    Space: O(n * goal)
    Time: O(n * goal)
    """
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # 점화식을 구성하여 문제 풀이
        # fn(m, l)는 현재 길이 l에서 m개의 노래로 만들 수 있는 플레이리스트의 수를 가리키고
        # fn(m, l) = fn(m-1, l-1) * m + fn(m, l-1) * (m-k) 이다
        # 1. fn(m-1, l-1) * m
        #    직전 길이 l-1에서 m-1개의 노래만을 포함하고 있다면 적어도 한 번 이상은 노래를 실행해야 하기 때문에
        #    직전 플레이리스트의 수에 선택할 수 있는 곡의 수 m을 곱함
        # 2. fn(m, l-1) * (m-k)
        #    직전 길이 l-1에서 이미 m개의 노래를 포함하고 있다면 현재에서는 k만큼을 제외한 곡들 중 하나를
        #    선택하여 플레이리스트에 담을 수 있기 때문에 m-k를 곱함

        mod = 10**9 + 7
        memo = [[-1 for _ in range(goal+1)] for _ in range(n+1)]

        for m in range(k+1, n+1):
            for l in range(m, goal+1):
                if (m == l) or (m == k+1):
                    memo[m][l] = math.factorial(m) % mod
                else:
                    memo[m][l] = (memo[m-1][l-1] * m + memo[m][l-1] * (m-k)) % mod
        
        return memo[n][goal]
