"""
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
"""
class Solution:
    """
    Keyword: Sort, Two Pointers
    Space: O(n)
    Time: O(max(nlogn, mlogm))
    """
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # 문제에서 원하는 것은 각 spell 당 조건에 부합하는 potion의 수이기 때문에
        # potions 리스트를 정렬하여 문제 접근해도 괜찮음
        # spells 리스트의 경우 정렬하려면 기존 인덱스 정보를 저장해놓아야 함

        n = len(spells)
        m = len(potions)

        my_spells = list()
        for i in range(n):
            my_spells.append((spells[i], i))
        
        my_spells.sort(key=lambda x: x[0])
        potions.sort(key=lambda x: -x)

        pairs = [0 for _ in range(n)]
        j = 0

        for spell, i in my_spells:
            while (j < m) and (spell*potions[j] >= success):
                j += 1
            pairs[i] = j

        return pairs
