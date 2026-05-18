class Solution {
public:
    void backtrack(int i, int sum, const vector<int>& nums, int target, vector<vector<int>>& ans, vector<int> tempNums){
        if(sum == target){
            ans.push_back(tempNums);
            return;
        }

        if(i >= nums.size() || sum > target) return;

        tempNums.push_back(nums[i]);
        //include that current guy, i.e dont update i
        backtrack(i, sum+nums[i], nums, target, ans, tempNums);
        tempNums.pop_back();
        //dont include that current guy, i.e 1+i
        backtrack(i+1, sum, nums, target, ans, tempNums);
    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        vector<int> tempNums;
        backtrack(0, 0, nums, target, ans, tempNums);
        return ans;
    }
};
