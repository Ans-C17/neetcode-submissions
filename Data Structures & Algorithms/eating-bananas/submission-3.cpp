class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = *max_element(piles.begin(), piles.end());
        int minK = high;

        while(low <= high){
            int mid = low + (high-low)/2;

            long long count = 0;
            for(const auto& elem : piles){
                count += ceil(static_cast<double>(elem)/mid);
            }

            if(count <= h){
                minK = mid;
                high = mid-1;
            }else low = mid+1;
        }

        return minK;
    }
};
