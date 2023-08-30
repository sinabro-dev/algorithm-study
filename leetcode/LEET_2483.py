"""
https://leetcode.com/problems/minimum-penalty-for-a-shop/description/

You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':
- if the ith character is 'Y', it means that customers come at the ith hour
- whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
- For every hour when the shop is open and no customers come, the penalty increases by 1.
- For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.
Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
- 1 <= customers.length <= 105
- customers consists only of characters 'Y' and 'N'

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
"""
class Solution:
    """
    Keyword: Prefix Sum, Memoization
    Space: O(n)
    Time: O(n)
    """
    def bestClosingTime(self, customers: str) -> int:
        # 역순으로 훑으면 이전 결과값을 이용해서 현재 결과를 구할 수 있음
        # 따라서 memoization 이용
        
        n = len(customers)

        memo = [0 for _ in range(n+1)]
        for log in customers:
            if log == 'N':
                memo[n] += 1
        
        best_hour, min_penalty = n, memo[n]

        for i in reversed(range(n)):
            prev = memo[i+1]
            if customers[i] == 'N':
                prev -= 1
            
            memo[i] = prev
            if customers[i] == 'Y':
                memo[i] += 1

            if memo[i] <= min_penalty:
                best_hour = i
                min_penalty = memo[i]
        
        return best_hour
