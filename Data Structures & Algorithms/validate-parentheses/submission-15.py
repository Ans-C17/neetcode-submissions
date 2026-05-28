class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)

            else:
                if not stack:
                    return False

                if stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                else:
                    return False

        return len(stack) == 0