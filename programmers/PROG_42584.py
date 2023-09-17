"""
https://school.programmers.co.kr/learn/courses/30/lessons/42584

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

prices	        return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
"""
def solution(prices):
    """
    Keyword: Monotonic Stack
    Space: O(n)
    Time: O(n)
    """
    n = len(prices)
    ret = [0 for _ in range(n)]
    
    stack = list()
    stack.append((prices[0], 0))
    
    for i in range(1, n):
        price = prices[i]
    
        while stack and price < stack[-1][0]:
            _, j = stack.pop()
            ret[j] = i - j
        
        stack.append((price, i))
    
    while stack:
        _, i = stack.pop()
        ret[i] = n - 1 - i
    
    return ret
