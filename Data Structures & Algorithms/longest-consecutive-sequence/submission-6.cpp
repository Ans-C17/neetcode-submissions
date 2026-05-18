class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) return 0;

        unordered_set<int> s;
        for(const auto& elem : nums) s.insert(elem);

        vector<int> vec(s.begin(), s.end());
        if(vec.size() == 1) return 1;
        sort(vec.begin(), vec.end());

        int max = 0;
        int i = 0;
        while(i < vec.size()-1){
            int count = 0;

            while(i+1 < vec.size() && vec[i+1]-vec[i] == 1){
                count++;
                i++;
            }

            if(count != 0) count++;
            else i++;
            if(count > max) max = count;
        }

        return max;
    }
};