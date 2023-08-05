"""
https://leetcode.com/problems/non-decreasing-subsequences/description/

Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
"""
class Solution:
    """
    Keyword: Backtracking
    Space: O(2^n)
    Time: O(2^n)
    """
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # nums 요소들을 훑으며 해당 요소를 반환할 리스트에 추가할지 말지를 결정
        # 리스트의 마지막 요소와 비교하여 non-decresing인 경우 선택 가능
        # 리스트의 마지막 요소와 비교하여 incresing인 경우 무조건 스킵
        # 모든 요소들을 훑었을 때 반환할 리스트의 길이가 2 이상이라면 답에 추가

        seqs_set = set()

        def walk_through(idx: int, target: list) -> None:
            if idx >= len(nums):
                if len(target) > 1:
                    seqs_set.add(tuple(target))
                return
            
            if (not target) or (nums[idx] >= target[-1]):
                target.append(nums[idx])
                walk_through(idx+1, target)
                target.pop()
            
            walk_through(idx+1, target)

        walk_through(0, [])
        
        seqs = list()
        for seq in seqs_set:
            seqs.append(list(seq))
        
        return seqs
