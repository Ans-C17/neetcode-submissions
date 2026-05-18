class Solution {
public:
    int dfs(vector<vector<int>>& grid, int r, int c, vector<vector<bool>>& visited) {
        if (r >= grid.size() || c >= grid[0].size() || r < 0 || c < 0 || !grid[r][c]) {
            return 1;
        }

        if (grid[r][c] && visited[r][c] == true) return 0;

        visited[r][c] = true;
        int perim = 0;
        perim += dfs(grid, r, c+1, visited) + dfs(grid, r+1, c, visited) + dfs(grid, r, c-1, visited) + dfs(grid, r-1, c, visited); 
        return perim;
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();

        vector<vector<bool>> visited(rows, vector<bool>(cols, false));

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c]) return dfs(grid, r, c, visited);
            }
        }

        return 0;
    }
};