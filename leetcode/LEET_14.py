"""
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
class Node:
    def __init__(self, key: str):
        self.key = key
        self.child = None

class Solution:
    """
    Keyword: Trie
    Space: O(1)
    Time: O(N)
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        head = None
        for char in reversed(strs[0]):
            node = Node(char)
            node.child = head
            head = node
        dummy = Node('')
        dummy.child = head
        head = dummy
        
        for pos in range(1, len(strs)):
            s = strs[pos]
            ptr = head
            idx = 0

            while True:
                if not ptr.child:
                    break
                if idx >= len(s):
                    break
                if ptr.child.key != s[idx]:
                    break

                ptr = ptr.child
                idx += 1
            
            ptr.child = None
        
        ret = list()
        ptr = head.child

        while ptr:
            ret.append(ptr.key)
            ptr = ptr.child

        return ''.join(ret)
