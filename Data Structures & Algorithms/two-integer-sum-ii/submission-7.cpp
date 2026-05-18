class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int slow = 0;
        int fast = numbers.size()-1;

        while(slow < fast){
            if((numbers[slow] + numbers[fast] == target) && (numbers[slow] != numbers[fast])) return {slow+1, fast+1};
            if(numbers[slow]+numbers[fast] <= target) slow++;
            else fast--;
        }

        return {};
    }
};
