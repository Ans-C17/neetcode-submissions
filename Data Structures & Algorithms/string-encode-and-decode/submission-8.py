class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += (str(len(word)) + "#" + word)
        
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j]) #to get multidigit nums
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j
        
        return res

        return res