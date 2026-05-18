class Solution {
public:
    int dfs(vector<vector<char>>& grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == '0') {
            return 0;
        }

        grid[r][c] = '0';

        if (dfs(grid, r+1, c) || dfs(grid, r, c+1) || dfs(grid, r, c-1) || dfs(grid, r-1, c)) {
            return 1;
        }

        return 0;
    }

    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }

        return count;
    }
};
