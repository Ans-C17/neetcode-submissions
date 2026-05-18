class Solution {
public:
    int trap(vector<int>& height) {
        if(height.empty()) return 0;

        int l = 0, r = height.size()-1;
        int maxL = height[l], maxR = height[r];
        int totalWater = 0;
        while(l < r){
            if(maxL < maxR){
                l++;
                maxL = max(maxL, height[l]);
                totalWater += maxL - height[l];
            }else{
                r--;
                maxR = max(maxR, height[r]);
                totalWater += maxR - height[r];
            }
        }

        return totalWater;
    }
};
