"""
https://leetcode.com/problems/walking-robot-simulation/description/

A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:
- -2: Turn left 90 degrees.
- -1: Turn right 90 degrees.
- 1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).
Note:
- North means +Y direction.
- East means +X direction.
- South means -Y direction.
- West means -X direction.

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.
"""
class Solution:
    """
    Keyword: Simulation
    Space: O(num_obstacles)
    Time: O(num_commands)
    """
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set()
        for pos in obstacles:
            x, y = pos[0], pos[1]
            obstacles_set.add((x, y))

        max_d = 0
        x, y = 0, 0
        dx, dy = 0, 1

        for cmd in commands:
            if cmd < 0:
                if dx != 0:
                    dy = 1 if (cmd*dx == 1) or (cmd*dx == -2) else -1
                    dx = 0
                else:
                    dx = 1 if (cmd*dy == -1) or (cmd*dy == 2) else -1
                    dy = 0
                continue
            
            for _ in range(1, cmd+1):
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in obstacles_set:
                    break
                
                x, y = next_x, next_y
                max_d = max(max_d, x**2 + y**2)

        return max_d
