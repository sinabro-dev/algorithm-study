"""
https://leetcode.com/problems/word-break/description/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
"""
class Solution:
    """
    Keyword: Trie, DP(Dynamic Programming)
    Space: O(num_word * word_size)
    Time: O(s_size * word_size)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Trie 구성 후, 트리 내의 가능한 단어들을 순차적으로 시도하는 흐름.
        # 이때 반복되는 연산을 막기 위해 메모이제이션을 활용.

        head = Node()

        for word in wordDict:
            head.insert(word)

        memo = [False for _ in range(len(s)+1)]
        memo[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if not memo[j]:
                    continue
                
                if head.search(s[j:i]):
                    memo[i] = True
                    break
        
        return memo[-1]
            
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
    
    def search(self, word: str) -> bool:
        node = self

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_word
