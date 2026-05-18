class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if(nums.empty()) return false;
        unordered_map<int, int> freq;
        for(int elem : nums){
            freq[elem]++;
            if(freq[elem] > 1) return true;
        }

        return false;
    }
};
