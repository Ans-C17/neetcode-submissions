class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1count, s2count = [0] * 26 , [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1count[i] == s2count[i] else 0
        
        l, r = 0, len(s1) # first three letters we added already
        while r < len(s2):
            if matches == 26:
                return True
                       
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] + 1 == s2count[index]: 
                matches -= 1
            
            # a = 2 and a = 6.. when a count was 2,1 match = 0... 2,2 made match = 1... so now 2, 3 makes it 0 again.. then u dont need to reduce it further for every mistmatch! 

            index = ord(s2[l]) - ord('a')
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s1count[index] - 1 == s2count[index]:
                matches -= 1
            
            l += 1
            r += 1

        return matches == 26