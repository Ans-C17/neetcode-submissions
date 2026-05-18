class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total, start = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
            
        return start

        #why shouldnt we wrap around? as we need only start point. bcoz if we know there exists a solution, it should be there anywhere in the diff array ... so total -ve avatha last guy (not necessarily last element of the array) would be a solution to this