"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/?envType=daily-question&envId=2023-09-12

A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.
The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
- 1 <= s.length <= 105
- s contains only lowercase English letters

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
"""
class Solution:
    """
    Keyword: Sorting, Greedy
    Space: O(n)
    Time: O(nlogn)
    """
    def minDeletions(self, s: str) -> int:
        # 알파벳별로 frequency 카운트 후 가장 높은 카운트부터 시작하여
        # 동일한 카운트의 경우 하나를 감소시키고 다음 카운트로 넘어가며 반복 수행

        from heapq import heappush, heappop

        freqs = dict()
        for char in s:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1

        heap = list()
        for char, freq in freqs.items():
            heappush(heap, (-freq, char))
        
        operation = 0
        completes = set()

        while heap:
            elem = heappop(heap)
            freq, char = -elem[0], elem[1]

            if freq == 0:
                continue

            if freq in completes:
                operation += 1
                heappush(heap, (-freq+1, char))
            else:
                completes.add(freq)
        
        return operation
