"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
class Solution:
    """
    Keyword: Backtracking
    Space: O(1)
    Time: O(N)
    """
    def letterCombinations(self, digits: str) -> List[str]:
        def combination(pos: int, case: str):
            if len(case) == len(digits):
                cases.append(case)
                return

            for idx in range(pos, len(digits)):
                for letter in mapping.get(digits[pos]):
                    combination(idx + 1, case + letter)

        if not digits:
            return list()
        
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        cases = list()

        combination(0, '')

        return cases
