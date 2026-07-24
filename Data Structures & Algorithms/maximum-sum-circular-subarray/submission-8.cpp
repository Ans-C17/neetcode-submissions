class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int total = nums[0];

        int curMax = nums[0], maxSum = nums[0];
        int curMin = nums[0], minSum = nums[0];

        for (int i = 1; i < nums.size(); i++) {
            total += nums[i];

            // Kadane for maximum subarray
            curMax = max(nums[i], curMax + nums[i]);
            maxSum = max(maxSum, curMax);

            // Kadane for minimum subarray
            curMin = min(nums[i], curMin + nums[i]);
            minSum = min(minSum, curMin);
        }

        // All numbers are negative - only one elem return as other neg elem gon worsen shi
        if (maxSum < 0)
            return maxSum;

        return max(maxSum, total - minSum);
    }
};