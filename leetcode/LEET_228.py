"""
https://leetcode.com/problems/summary-ranges/description/

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""
class Solution:
    """
    Keyword: Two Pointer
    Space: O(1)
    Time: O(n)
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return list()

        ret = list()
        start, end = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                continue
            
            end = nums[i-1]
            
            if start == end:
                ret.append(f'{start}')
            else:
                ret.append(f'{start}->{end}')
            
            start = nums[i]

        if start == nums[-1]:
            ret.append(f'{start}')
        else:
            ret.append(f'{start}->{nums[-1]}')

        return ret
