class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} 
        res = []

        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        size = end = 0
        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res