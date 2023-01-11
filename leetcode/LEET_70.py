"""
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    """
    Keyword: Combination
    Space: O(1)
    Time: O(N)
    """
    def climbStairs(self, n: int) -> int:
        # `n`을 1과 2로 표현할 수 있는 조합 경우를 구한 후,
        # 각 경우에서 1과 2들을 줄 세우는 경우를 모두 더하는 흐름.
        # 이때 그룹핑한 순열로, (n + m)! / (n! * m!) 이용.

        def mul_rng(start: int, end: int) -> int:
            ret = 1
            for num in range(start, end+1):
                ret *= num
            return ret

        ret = 0
        two_cnt = n // 2

        while two_cnt >= 0:
            one_cnt = n - 2 * two_cnt

            cases = mul_rng(one_cnt+1, one_cnt+two_cnt) / mul_rng(1, two_cnt)
            ret += int(cases)
            
            two_cnt -= 1
        
        return ret
