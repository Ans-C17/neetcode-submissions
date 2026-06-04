class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        endIndex = {}
        for i in range(len(s)):
            endIndex[s[i]] = i

        size = end = 0
        for i in range(len(s)):
            end = max(end, endIndex[s[i]])
            size += 1
            
            if i == end:
                res.append(size)
                size = 0
        
        return res