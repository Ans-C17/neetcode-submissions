class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_set<int> s;
        int j = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (s.count(nums[i])) {
                while (j < nums.size() and s.count(nums[j])) j++;
                if (j == nums.size()) return i;
                int tmp = nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
            }

            s.insert(nums[i]);
        }

        return nums.size();
    }
};