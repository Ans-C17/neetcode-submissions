class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maxTriplet = [0, 0, 0]
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                maxTriplet[0] = max(maxTriplet[0], t[0])
                maxTriplet[1] = max(maxTriplet[1], t[1])
                maxTriplet[2] = max(maxTriplet[2], t[2])
                
            if maxTriplet == target:
                return True

        return False