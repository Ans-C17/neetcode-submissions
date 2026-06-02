class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:] # if the end is less than the start of the next interval, then obviously it is going to be less than every single upcoming interval because the next start is greater than the previous start for sure
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i]) # start can be greater than next ends, so cant return as interval might fit aptly further ahead only
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                # we update the value of interval, not insert it yet
        
        res.append(newInterval) # it would have returned beforehand, if it didnt, we append to the end
        return res