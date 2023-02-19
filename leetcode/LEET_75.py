"""
https://leetcode.com/problems/sort-colors/description/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
class Solution:
    """
    Keyword: Sorting, Two Pointers
    Space: O(1)
    Time: O(n)
    """
    def sortColors(self, nums: List[int]) -> None:
        # 먼저 중심 자리를 차지할 white 요소들을 찾아서 올바른 위치로 정렬 후,
        # 앞부분에 blue 요소인 것들을 뒷부분에 red 요소인 것과 교체하는 흐름.
        
        reds, whites, blues = 0, 0, 0

        for num in nums:
            if num == 0:
                reds += 1
            elif num == 1:
                whites += 1
            elif num == 2:
                blues += 1
        
        ptr = reds

        for idx in range(0, reds):
            if nums[idx] != 1:
                continue
            
            while (reds <= ptr < reds+whites):
                if nums[ptr] != 1:
                    break
                ptr += 1
            
            nums[idx], nums[ptr] = nums[ptr], nums[idx]
        
        for idx in range(reds+whites, reds+whites+blues):
            if nums[idx] != 1:
                continue
            
            while (reds <= ptr < reds + whites):
                if nums[ptr] != 1:
                    break
                ptr += 1
            
            nums[idx], nums[ptr] = nums[ptr], nums[idx]

        ptr = reds + whites

        for idx in range(0, reds):
            if nums[idx] != 2:
                continue
            
            while (reds+whites <= ptr < reds+whites+blues):
                if nums[ptr] != 2:
                    break
                ptr += 1
            
            nums[idx], nums[ptr] = nums[ptr], nums[idx]
