class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> freq;

        for(int i : nums) freq[i]++;
        for(int i; i < nums.size(); ++i){
            if(target-nums[i] == nums[i] && freq[target-nums[i]] > 1){
                int j = i+1;
                while(nums[j] != target-nums[i]) j++;
                return {i, j};
            }else if(target-nums[i] != nums[i] && freq[target-nums[i]] > 0){
                int j = i;
                while(nums[j] != target-nums[i]) j++;
                return {i, j};
            }
        }
    }
};
