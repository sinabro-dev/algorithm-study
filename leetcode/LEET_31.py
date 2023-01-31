"""
https://leetcode.com/problems/next-permutation/description/

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
- For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
- For example, the next permutation of arr = [1,2,3] is [1,3,2].
- Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
- While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
- Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

Input: nums = [1,2,3]
Output: [1,3,2]
"""
class Solution:
    """
    Keyword: Two Pointers, Simulation
    Space: O(1)
    Time: O(n)
    """
    def nextPermutation(self, nums: List[int]) -> None:
        # `nums`의 구성 요소 중에서 변곡점이 되는 부분은 정렬이 끊기는 부분.
        # 맨 뒤 요소부터 시작하여 역순으로 훑으며,
        # 수가 점점 커지는 부분까지 추적하여 끊기는 부분을 찾고,
        # 해당 지점의 앞 수를 포함하여 다음 순열을 찾는 흐름.

        length = len(nums)
        
        if length == 1:
            return
        
        i = length - 1

        while True:
            if i == 0:
                break
            if nums[i - 1] < nums[i]:
                break
            i -= 1

        for k in range((length - i) // 2 + (length - i) % 2):
            p = i + k
            q = length - 1 - k
            nums[p], nums[q] = nums[q], nums[p]

        if i != 0:
            j = i
            while nums[j] <= nums[i - 1]:
                j += 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
