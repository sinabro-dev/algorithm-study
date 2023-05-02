"""
https://leetcode.com/problems/permutation-in-string/description/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
"""
class Solution:
    """
    Keyword: Sliding Window
    Space: O(1)
    Time: O(n)
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2를 s1 크기의 윈도우로 훑으며 부분 문자열이 s1의 모든 문자를 포함하는지 확인

        from collections import defaultdict

        char_cnt = defaultdict(int)
        for char in s1:
            char_cnt[char] += 1
        
        match = 0

        for idx in range(len(s2)):
            if s2[idx] in char_cnt:
                if char_cnt[ s2[idx] ] > 0:
                    match += 1
                char_cnt[ s2[idx] ] -= 1
            
            if (idx >= len(s1)) and (s2[idx-len(s1)] in char_cnt):
                char_cnt[ s2[idx-len(s1)] ] += 1
                if char_cnt[ s2[idx-len(s1)] ] > 0:
                    match -= 1
            
            if match == len(s1):
                return True

        return False

class StuckSolution:
    def checkInclusion(self, s1: str, s2: str) -> None:
        # s1 길이만큼의 s2의 서브 문자열의 수보다 s1 순열 경우의 수가 훨씬 크기 때문에
        # s2의 서브 문자열들을 먼저 구하고 s1 순열 경우가 그 중 하나인지 확인하도록
        # 그럼에도 불필요한 연산이 많으므로 필요없는 순열 경우는 조기에 중단하도록 Trie 사용

        if len(s1) > len(s2):
            return False
        
        head = Node()

        for idx in range(0, len(s2)-len(s1)+1):
            sub_str = s2[idx : idx+len(s1)]
            head.insert(sub_str)
    
        idx_set = {idx for idx in range(len(s1))}
        stack = [(char, {idx}) for idx, char in enumerate(s1)]

        while stack:
            case, sub_idx = stack.pop()

            if len(case) == len(s1):
                if head.search(case) == 2:
                    return True
                else:
                    continue
            
            if head.search(case) == 0:
                continue
            
            for idx in (idx_set-sub_idx):
                next_case = ''.join([case, s1[idx]])
                next_idx = sub_idx.copy()
                next_idx.add(idx)
                stack.append((next_case, next_idx))

        return False
    
class Node:
    def __init__(self):
        self.is_word = False
        self.children = dict()
    
    def insert(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        
        node.is_word = True
    
    def search(self, word: str) -> int:
        node = self

        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        
        if not node.is_word:
            return 1
        else:
            return 2
