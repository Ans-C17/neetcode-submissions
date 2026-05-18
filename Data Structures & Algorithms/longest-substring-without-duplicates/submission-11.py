class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        seen = set()

        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[left])
                    left += 1
            
            seen.add(s[r])
            longest = max(longest, r - left + 1)
        
        return longest