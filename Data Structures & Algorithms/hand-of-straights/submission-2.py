class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for h in hand:
            count[h] = 1 + count.get(h, 0)
        
        heap = list(count.keys())
        heapq.heapify(heap)
        while heap:
            elem = heap[0]
            for i in range(elem, elem + groupSize):
                if i not in count:
                    return False
               
                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        
        return True