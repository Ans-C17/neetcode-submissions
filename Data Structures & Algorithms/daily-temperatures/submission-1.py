class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(temperatures)

        for i in range(len(temperatures)):
            if stack and temperatures[i] > stack[-1][0]:
                while stack and temperatures[i] > stack[-1][0]:
                    elem = stack.pop()
                    ind = elem[1]
                    res[ind] = i - ind

            stack.append((temperatures[i], i))
        
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = 0
        
        return res