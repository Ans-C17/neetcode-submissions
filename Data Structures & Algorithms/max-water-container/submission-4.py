class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxArea = 0
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            maxArea = max(maxArea, area)
            if min(heights[i], heights[j]) == heights[i]:
                i += 1
            else:
                j -= 1
        return maxArea