class Solution {
public:
    int findMin(vector<int> &nums) {
        int low = 0;
        int high = nums.size() - 1;
        int minElem = 1001;

        while(low <= high){
            int mid = low + (high-low)/2;
            minElem = min(minElem, nums[mid]);

            if(nums[mid] >= nums[high]) low = mid + 1;
            else high = mid - 1;
        }

        return minElem;
    }
};
