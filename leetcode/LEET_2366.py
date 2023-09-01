"""
https://leetcode.com/problems/minimum-replacements-to-sort-the-array/description/?envType=daily-question&envId=2023-08-30

You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.
- For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 109

Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.
"""
class Solution:
    """
    Keyword: Greedy, Math
    Space: O(1)
    Time: O(n)
    """
    def minimumReplacement(self, nums: List[int]) -> int:
        # 최종적으로 리스트는 순서대로 같거나 큰, 오름차순으로 정렬되어야 하기 때문에
        # 마지막 요소는 문제에서 말하는 operation을 수행하지 않도록 하는 것이 optimal한 경우
        # 이 점을 이용해서 nums[-2] 요소부터 operation 수행 후 더이상 쪼개지지 않도록 하는 경우를 찾아야 함

        n = len(nums)
        cnt = 0
        last = nums[n-1]

        for i in range(n-2, -1, -1):
            if nums[i] <= last:
                last = nums[i]
                continue
            
            k = nums[i] // last
            if nums[i] % last:
                k += 1
            
            cnt += k-1
            last = nums[i] // k
        
        return cnt
