class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(heights)-1

        while left < right:
            minHeight = min(heights[right], heights[left])
            maxArea = max(maxArea, minHeight * (right - left))
            if minHeight == heights[right]:
                right -= 1
            else:
                left += 1
        
        return maxArea