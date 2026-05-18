class Solution {
public:
    int dfs(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || !grid[r][c]) {
            return 0;
        }

        grid[r][c] = 0;

        int area = 0;
        area += 1 + dfs(grid, r, c+1) + dfs(grid, r+1, c) + dfs(grid, r, c-1) + dfs(grid, r-1, c);

        return area;
    }

    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    int area = dfs(grid, i, j);
                    maxArea = max(maxArea, area);
                }
            }
        }

        return maxArea;
    }
};
