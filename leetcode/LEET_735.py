"""
https://leetcode.com/problems/asteroid-collision/description/

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""
class Solution:
    """
    Keyword: Simulation
    Space: O(1)
    Time: O(n^2)
    """
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 충돌이 발생할 수 있는 곳은 asteroid 부호가 양수에서 음수로 바뀔 때
        # 부호가 음수에서 양수로 바뀔 때는 서로 멀어지기 때문에 충돌 발생하지 않음
        # 마주보고 움직이는 asteroid들에 대해서 일어날 수 있는 충돌들을 모두 확인 후
        # 다음 충돌 발생할 수 있는 곳으로 이동

        states = list()

        for i in range(len(asteroids)):
            cur = asteroids[i]

            if cur > 0:
                continue
            
            for j in reversed(range(i)):
                prev = asteroids[j]

                if prev == 0:
                    continue
                
                if prev*cur > 0:
                    break
                
                if prev < -cur:
                    asteroids[j] = 0
                    continue
                
                if prev > -cur:
                    asteroids[i] = 0
                    break
                
                if prev == -cur:
                    asteroids[i] = 0
                    asteroids[j] = 0
                    break
        
        states = list()
        for asteroid in asteroids:
            if asteroid == 0:
                continue
            states.append(asteroid)

        return states
