class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        vector<int> cur;
        backtrack(nums, target, result, cur, 0);
        return result;
    }

private:
    void backtrack(vector<int>& nums, int target, vector<vector<int>>& result, vector<int>& cur, int i) {
        if (target == 0) {
            result.push_back(cur);
            return;
        }

        if (target < 0 || i >= nums.size()) return;

        cur.push_back(nums[i]);
        // target -= nums[i];
        backtrack(nums, target - nums[i], result, cur, i);
        cur.pop_back();
        backtrack(nums, target, result, cur, i+1);
    }
};
