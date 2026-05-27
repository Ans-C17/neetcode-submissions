class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        hand.sort()
        count = Counter(hand)

        for i in range(len(hand)):
            if count[hand[i]] > 0:
                for j in range(hand[i], hand[i] + groupSize):
                    if count[j] <= 0:
                        return False

                    count[j] -= 1
        
        return True