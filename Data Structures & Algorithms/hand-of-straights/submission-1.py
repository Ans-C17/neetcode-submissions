class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        vals = {}
        for c in hand:
            vals[c] = 1 + vals.get(c, 0)

        minheap = list(vals.keys())
        heapq.heapify(minheap)

        while minheap:
            minval = minheap[0]
            for i in range(minval, minval + groupSize):
                if i not in vals:
                    return False
                
                vals[i] -= 1
                if vals[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
            
        return True