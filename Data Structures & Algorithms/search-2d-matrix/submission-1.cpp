class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int low = 0;
        int high = matrix.size()*matrix[0].size()-1;
        int n = matrix[0].size();
        while(low <= high){
            int mid = low + (high - low)/2;
            //index/n = row number.
            //index%n = coloumn number.
            if(matrix[mid/n][mid%n] == target) return true;
            if(matrix[mid/n][mid%n] < target) low = mid+1;
            else high = mid - 1;
        }

        return false;
    }
};
