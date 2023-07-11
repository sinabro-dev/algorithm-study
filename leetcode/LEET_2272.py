"""
https://leetcode.com/problems/substring-with-largest-variance/description/

The variance of a string is defined as the largest difference between the number of occurrences of any 2 characters present in the string. Note the two characters may or may not be the same.
Given a string s consisting of lowercase English letters only, return the largest variance possible among all substrings of s.
A substring is a contiguous sequence of characters within a string.

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
"""
class Solution:
    """
    Keyword: Divide and Conquer
    Space: O(n)
    Time: O(n)
    """
    def largestVariance(self, s: str) -> int:
        # 만약 s가 두 종류의 문자로만 이뤄졌다면 한 문자를 만날 때 +1, 다른 문자는 -1 해서 variance를 구하면 된다
        # 그러나 알파벳 26개로 이뤄질 수 있기 때문에 이에 대한 상태 관리가 필요하다
        # 또한 모든 서브스트링을 훑을 것이기 때문에 반복 작업을 피하기 위해 다이나믹 프로그래밍으로 접근한다
        # ----------------------------------------------------------------------------------------------------
        # 위의 방식대로 하면 답을 구하겠으나 시간 초과가 뜬다
        # 문제 해결을 위해 주요한 두 값은 서브스트링의 최소 등장 알파벳과 최대 등장 알파벳이다
        # 이를 위해 N^2 반복을 하며 모두 확인하는 것보다는 문자열을 순행와 역행하여 각 등장 수를 체크하는 방법이 있다
        # 이때 모든 알파벳 조합을 체크해야 하므로 유일한 알파벳 쌍들을 만들어놓고 시작해야 한다

        max_var = 0

        pairs = list()
        for a in set(s):
            for b in set(s):
                if a == b:
                    continue
                pairs.append((a, b))
        

        for _ in range(2):
            for pair in pairs:
                cnt_a, cnt_b = 0, 0

                for char in s:
                    if char not in pair:
                        continue
                    
                    if char == pair[0]:
                        cnt_a += 1
                    else:
                        cnt_b += 1
                    
                    if cnt_a < cnt_b:
                        cnt_a, cnt_b = 0, 0
                    elif cnt_a > 0 and cnt_b > 0:
                        max_var = max(max_var, cnt_a - cnt_b)

            s = s[::-1]
        
        return max_var
