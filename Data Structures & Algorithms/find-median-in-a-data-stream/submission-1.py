class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        if len(self.leftMaxHeap) > len(self.rightMinHeap):
            heapq.heappush(self.rightMinHeap, num)
        else:
            heapq.heappush(self.leftMaxHeap, -num)
        
        if self.rightMinHeap and self.leftMaxHeap:
            if self.rightMinHeap[0] < -self.leftMaxHeap[0]:
                temp = heapq.heappop(self.leftMaxHeap)
                heapq.heappush(self.leftMaxHeap, -heapq.heappop(self.rightMinHeap))
                heapq.heappush(self.rightMinHeap, -temp)

    def findMedian(self) -> float:
        if len(self.leftMaxHeap) == len(self.rightMinHeap):
            return (-self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2
        else:
            return -self.leftMaxHeap[0]