"""
https://leetcode.com/problems/sliding-window-maximum/description/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
class Solution:
    """
    Keyword: Heap, Sliding Window
    Space: O(n)
    Time: O(n)
    """
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 최대힙을 구성하여 윈도우에 추가되는 요소를 삽입.
        # 힙에 삭제되어야 하는 요소에 대해서는 실제로 삭제하기보다는
        # 별도의 해시맵으로 존재 여부를 확인하도록 함.
        # 이를 위해서는 힙에 중복 요소가 존재하지 않아야 함.

        import heapq

        hq = list()
        cnt_map = dict()
        ret = list()

        for i in range(k):
            num = nums[i]
            if not num in cnt_map:
                cnt_map.update({num: 1})
                heapq.heappush(hq, -num)
            else:
                cnt_map.update({num: cnt_map.get(num) + 1})
        
        ret.append(-hq[0])

        for i in range(k, len(nums)):
            old_num = nums[i - k]
            cnt_map.update({old_num: cnt_map.get(old_num) - 1})

            new_num = nums[i]
            if (not new_num in cnt_map) or (cnt_map.get(new_num) == 0):
                cnt_map.update({new_num: 1})
                heapq.heappush(hq, -new_num)
            else:
                cnt_map.update({new_num: cnt_map.get(new_num) + 1})
            
            while cnt_map.get(-hq[0]) == 0:
                heapq.heappop(hq)

            ret.append(-hq[0])
        
        return ret
