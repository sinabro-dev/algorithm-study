"""
https://leetcode.com/problems/fair-distribution-of-cookies/description/

You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.
The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.
Return the minimum unfairness of all distributions.

Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.
"""
class Solution:
    """
    Keyword: Dynamic Programming, Bit Manipulation
    Space: O(k * n)
    Time: O(k * 2**n)
    """
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # cookies 리스트의 최대 길이가 8인 점을 고려하면
        # 분배하는 모든 경우를 비트마스킹으로 표현해도 무방하다
        # 비트의 각 자리로 분배여부를 표현하고 k번 만큼 반복하여 완료될 때
        # 나눠준 쿠키의 수 최댓값을 알아냄을 반복한다
        # 이때 반복 계속이 많으므로 이전 결과값을 기록해둔다
        # i명한테 분배한 쿠키 가방들, 이 정보를 토대로 dp[i][bag_mask] 형태로 기록한다

        n = len(cookies)
        memo = [[-1] * (1<<n) for _ in range(k+1)]

        def sum_cookies(mask: int) -> int:
            total = 0
            for i in range(n):
                if mask & (1<<i):
                    total += cookies[i]
            return total

        def distribute(num, mask: int) -> int:
            if memo[num][mask] != -1:
                return memo[num][mask]
            
            if num == 1:
                memo[num][mask] = sum_cookies(mask)
                return memo[num][mask]
            
            bit = mask
            ans = 10**5 * 8

            while bit > 0:
                sum1 = sum_cookies(bit)
                sum2 = distribute(num-1, bit^mask)

                ans = min(ans, max(sum1, sum2))

                bit = (bit-1) & mask
            
            
            memo[num][bit] = ans
            return ans
        
        return distribute(k, (1<<n)-1)
