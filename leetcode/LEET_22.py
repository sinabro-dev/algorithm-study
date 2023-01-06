"""
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
class Solution:
    """
    Keyword: Dynamic Programming (DP), Backtracking
    Space: O(N^2)
    Time: O(N^2)
    """
    def generateParenthesis(self, n: int) -> List[str]:
        case_set = set(['()'])

        for i in range(1, n):
            prev_cases = list(case_set)
            pos_num = 2*i + 1
            case_set = set()

            for prev_case in prev_cases:
                for pos in range(pos_num):
                    cur_case = prev_case[:pos] + '()' + prev_case[pos:]
                    case_set.add(cur_case)

        return case_set
