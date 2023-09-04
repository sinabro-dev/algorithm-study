"""
https://leetcode.com/problems/extra-characters-in-a-string/description/?envType=daily-question&envId=2023-09-02

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.
Return the minimum number of extra characters left over if you break up s optimally.
- 1 <= s.length <= 50
- 1 <= dictionary.length <= 50
- 1 <= dictionary[i].length <= 50
- dictionary[i] and s consists of only lowercase English letters
- dictionary contains distinct words
 
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
"""
class Solution:
    """
    Keyword: Trie, Dynamic Programming
    Space: O(len(dict))
    Time: O(n^2)
    """
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Trie 구조를 이용해서 s의 substring이 존재하는지 확인
        # 각 경우마다 상태값 기록을 위해 memoization 활용
        # memo(i) = s[i:]에서의 extra character 수를 의미

        n = len(s)

        head = Node()
        for word in dictionary:
            head.insert(word)
        
        memo = [51 for _ in range(n+1)]
        memo[-1] = 0

        for start in reversed(range(n)):
            memo[start] = memo[start+1] + 1

            for end in range(start, n):
                if head.search(s[start:end+1]):
                    memo[start] = min(memo[start], memo[end+1])
        
        return memo[0]
        

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
