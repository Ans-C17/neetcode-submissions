class NumMatrix {
private:
    vector<vector<int>> matrix;
    vector<vector<int>> prefix;

public:
    NumMatrix(vector<vector<int>>& matrix) {
        this->matrix = matrix;
        prefix.resize(matrix.size(), vector<int>(matrix[0].size()));

        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                prefix[i][j] = matrix[i][j];
                if (j > 0) prefix[i][j] += prefix[i][j - 1];
                if (i > 0) prefix[i][j] += prefix[i - 1][j];
                if (i > 0 and j > 0) prefix[i][j] -= prefix[i - 1][j - 1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int curr = prefix[row2][col2];
        int left = 0;
        int right = 0;
        int add = 0;

        if (row1 - 1 >= 0) right = prefix[row1 - 1][col2];
        if (col1 - 1 >= 0) left = prefix[row2][col1 - 1];
        if (row1 - 1 >= 0 and col1 - 1 >= 0) add = prefix[row1 - 1][col1 - 1];

        return prefix[row2][col2] - right - left + add;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */