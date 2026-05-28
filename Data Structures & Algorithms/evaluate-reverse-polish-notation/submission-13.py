class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in "+-/*":
                stack.append(int(char))
            else:
                val = 0
                one = stack.pop()
                two = stack.pop()
                
                if char == '+':
                    val = two + one
                elif char == '-':
                    val = two - one
                elif char == '*':
                    val = two * one
                else:
                    val = int(two / one)
                
                stack.append(val)
        
        return stack[-1]