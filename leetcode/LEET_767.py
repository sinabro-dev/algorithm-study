"""
https://leetcode.com/problems/reorganize-string/description/

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.
- 1 <= s.length <= 500
- s consists of lowercase English letters.

Input: s = "aaab"
Output: ""
"""
class Solution:
    """
    Keyword: Heap, Priority Queue, Greedy
    Space: O(n)
    Time: O(nlogn)
    """
    def reorganizeString(self, s: str) -> str:
        # 문자열을 훑으며 인접한 두 문자가 같은 경우
        # 해당 위치로부터 맨 끝까지 이루어진 문자들 중 현재 위치의 문자를 제외하고
        # 가장 많이 위치한 문자로 교체하며 진행
        # 최대힙 자료구조 이용

        from heapq import heappush, heappop

        mapper = defaultdict(int)
        for c in s:
            mapper[c] += 1

        heap = list()
        for char, cnt in mapper.items():
            heappush(heap, (-cnt, char))

        tgt = list()
        prev_val, prev_char = 0, ''

        while heap:
            cur_val, cur_char = heappop(heap)
            tgt.append(cur_char)

            if prev_val < 0:
                heappush(heap, (prev_val, prev_char))
            
            cur_val += 1
            prev_val, prev_char = cur_val, cur_char
        
        ret = ''.join(tgt)

        if len(ret) != len(s):
            return ''
        return ret
