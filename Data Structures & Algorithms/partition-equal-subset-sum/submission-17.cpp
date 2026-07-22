class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 2 != 0) return false;
        int target = sum / 2;

        unordered_set<int> s;
        s.insert(nums[nums.size() - 1]);
        s.insert(0);
        for (int i = nums.size() - 2; i >= 0; i--) {
            unordered_set<int> next = s;
            for (auto& elem : s) {
                if (s.count(target)) return true;
                int n = nums[i] + elem;
                if (n <= target) next.insert(n);
            }
            
            s = move(next);
        }

        return false;
    }
};
