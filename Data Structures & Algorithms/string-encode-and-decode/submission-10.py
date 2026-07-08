class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        start = 0
        i = 0

        res = []
        length = 0
        while i < len(s):
            while s[i] != '#':
                i += 1
            length = int(s[start : i])
            res.append(s[i + 1 : i + 1 + length])

            start = i + length + 1
            i = start

        return res

