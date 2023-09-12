"""
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/?envType=daily-question&envId=2023-09-11

There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.
You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.
Return a list of groups such that each person i is in a group of size groupSizes[i].
Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.
- groupSizes.length == n
- 1 <= n <= 500
- 1 <= groupSizes[i] <= n

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
"""
class Solution:
    """
    Keyword: Greedy, Hash Table
    Space: (n)
    Time: (nlogn)
    """
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # group 크기별로 정렬하는데 person 인덱스값을 기록하여 정렬 후,
        # 같은 크기에 속한 사람들끼리 묶어서 반환할 리스트에 담아 줌

        n = len(groupSizes)
        arr = [(groupSizes[idx], idx) for idx in range(n)]
        arr.sort(key=lambda x: (x[0], x[1]))
        arr.append((501, n))

        ret = list()
        group = list()
        target = arr[0][0]

        for size, idx in arr:
            if target != size:
                ret.append(group)
                group = list()
                target = size
            
            if len(group) == size:
                ret.append(group)
                group = list()
            
            group.append(idx)

        return ret
