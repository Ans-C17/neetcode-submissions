"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]

        start.sort()
        end.sort()

        l = r = 0
        res = 0
        count = 0
        while l < len(start):
            if start[l] < end[r]:
                count += 1
                l += 1
            else:
                count -= 1
                r += 1
            res = max(res, count)
        return res

