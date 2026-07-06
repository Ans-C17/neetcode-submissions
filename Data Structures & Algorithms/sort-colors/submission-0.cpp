class Solution {
public:
    void sortColors(vector<int>& nums) {
        int bucket[3] = {0, 0, 0};
        for (int elem : nums) {
            bucket[elem]++;
        }

        int i = 0;
        int j = 0;
        while (i < nums.size()) {
            while (bucket[j]) {
                nums[i] = j;
                bucket[j]--;
                i++;
            }
            j++;
        }
    }
};