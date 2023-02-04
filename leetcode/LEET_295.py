"""
https://leetcode.com/problems/find-median-from-data-stream/description/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""
# 작은 수로 이루어진 최대힙과 큰 수로 이루어진 최소힙을 유지하며,
# 중간값을 알기 위해서는 각 힙의 루트값을 비교 및 반환함.
# 이때 최대힙의 루트값이 최소힙의 루트값보다 작아야 함.
class MedianFinder:
    import heapq

    """
    Keyword: Heap, Two Pointers
    Space: O(n)
    """
    def __init__(self):
        self.smalls = list()
        self.bigs = list()
    
    """
    Time: O(log n)
    """
    def addNum(self, num: int) -> None:
        if len(self.smalls) == 0:
            heapq.heappush(self.smalls, -num)
            return
        if len(self.bigs) == 0:
            tmp = -heapq.heappop(self.smalls)
            heapq.heappush(self.smalls, -min(tmp, num))
            heapq.heappush(self.bigs, max(tmp, num))
            return

        if len(self.smalls) <= len(self.bigs):
            heapq.heappush(self.smalls, -num)
        else:
            heapq.heappush(self.bigs, num)
        
        if -self.smalls[0] <= self.bigs[0]:
            return

        if len(self.smalls) == len(self.bigs):
            small = -heapq.heappop(self.smalls)
            big = heapq.heappop(self.bigs)
            heapq.heappush(self.smalls, -big)
            heapq.heappush(self.bigs, small)
        else:
            num = -heapq.heappop(self.smalls)
            heapq.heappush(self.bigs, num)

    """
    Time: O(1)
    """
    def findMedian(self) -> float:
        smalls_size = len(self.smalls)
        bigs_size = len(self.bigs)

        if (smalls_size + bigs_size) % 2 == 0:
            return (-self.smalls[0] + self.bigs[0]) / 2
        elif smalls_size > bigs_size:
            return -self.smalls[0]
        else:
            return self.bigs[0]
