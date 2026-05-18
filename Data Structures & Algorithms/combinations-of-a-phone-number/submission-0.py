class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        res = []

        def backtrack(curr, i):
            if i == len(digits):
                res.append("".join(curr))
                return

            for letter in hashmap[digits[i]]:
                curr.append(letter)
                backtrack(curr, i + 1)
                curr.pop()
        
        # Step 3: handle edge case for empty input
        if not digits:
            return []

        curr = []
        backtrack(curr, 0)

        return res
            