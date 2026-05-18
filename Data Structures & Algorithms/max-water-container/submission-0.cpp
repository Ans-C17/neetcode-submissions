class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;
        int maxArea = 0;

        while(left < right){
            int minHeight = min(heights[left], heights[right]);
            int area = (minHeight * (right - left));
            maxArea = max(maxArea, area);
            minHeight == heights[left] ? left++ : right--;
        }

        return maxArea;
    }
};
