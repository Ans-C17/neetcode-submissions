class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        keylist = self.timemap[key]
        l, r = 0, len(keylist) - 1
        res = ""
        
        while l <= r:
            m = (l + r) // 2
            if keylist[m][1] <= timestamp:
                res = keylist[m][0]
                l = m + 1
            elif keylist[m][1] > timestamp:
                r = m - 1
        return res