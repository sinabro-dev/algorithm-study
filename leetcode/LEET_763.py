"""
https://leetcode.com/problems/partition-labels/description/

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
"""
class Solution:
    """
    Keyword: Tow Pointers
    Space: O(1)
    Time: O(N)
    """
    def partitionLabels(self, s: str) -> List[int]:
        # 알파벳 별로 어느 index들에 위치하는지 맵핑한 후,
        # 각 index 최댓값을 토대로 `s` 맨 앞에서부터 반복하며 그룹핑

        last_pos_map = dict()

        for pos, char in enumerate(s):
            last_pos_map[char] = pos

        ret = list()
        prev_pos = 0
        cur_pos = 0
        limit_pos = last_pos_map.get(s[0])

        while True:
            if cur_pos > limit_pos:
                ret.append(cur_pos - prev_pos)
                prev_pos = cur_pos
                
                if cur_pos >= len(s):
                    break

            last_pos = last_pos_map.get(s[cur_pos])
            limit_pos = last_pos if last_pos > limit_pos else limit_pos
            cur_pos += 1

        return ret
