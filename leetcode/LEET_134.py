"""
https://leetcode.com/problems/gas-station/description/

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
"""
class Solution:
    """
    Keyword: Greedy
    Space: O(1)
    Time: O(N)
    """
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 그리디 문제로 예상.
        # 매 경우 진행해보면서, 아니다 싶으면 바로 다음 경우로 넘어가는 흐름.
        # 이때 가능한 경우는 **오로지 1개** 이므로 `gas` 총합이 `cost` 총합보다 큰 경우,
        # 문제의 조건을 충족하는 경우 **하나만** 찾아내면 되는 것에 유의.

        if sum(gas) < sum(cost):
            return -1
        
        start, remain = 0, 0
        for pos in range(len(gas)):
            if remain + gas[pos] - cost[pos] < 0:
                start = pos + 1
                remain = 0
            else:
                remain += (gas[pos] - cost[pos])
        
        return start
