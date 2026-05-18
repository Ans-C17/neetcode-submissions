class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> result;
        for(int i = 0; i < nums.size(); ++i){
            if(nums[i] > 0) break;
            if(i > 0 && nums[i] == nums[i-1]) continue;

            int j = i+1;
            int k = nums.size()-1;
            while(j < k){
                if(nums[j]+nums[k] < -nums[i]) j++;
                else if(nums[j]+nums[k] > -nums[i]) k--;
                else{
                    result.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    k--;
                    while(j < k && nums[j] == nums[j-1]) j++;
                }
            }
        }

        return result;
    }
};