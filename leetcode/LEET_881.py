"""
https://leetcode.com/problems/boats-to-save-people/description/

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
"""
class Solution:
    """
    Keyword: Sort, Two Pointers
    Space: O(1)
    Time: O(nlogn)
    """
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # people 리스트를 정렬한 후
        # 맨 앞과 맨 뒤를 가리키는 두 개의 포인터를 이용해서
        # 조건에 맞는 짝을 찾아내는 작업을 반복

        people.sort(key=lambda x: -x)
        print(people)

        need = 0
        front, back = 0, len(people)-1

        while front < back:
            if people[front]+people[back] <= limit:
                front += 1
                back -= 1
            else:
                front += 1
            need += 1
        
        if front == back:
            need += 1

        return need
