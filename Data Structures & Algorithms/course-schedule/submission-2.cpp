class Solution {
public:
    bool dfs(int src, vector<vector<int>>& adjList, vector<bool>& visited, vector<bool>& path) {
        visited[src] = true;
        path[src] = true;

        for (auto& nei : adjList[src]) {
            if (path[nei]) return false; 
            if (!visited[nei]) {
                if (!dfs(nei, adjList, visited, path))
                    return false;
            }
        }

        path[src] = false;
        return true;
    }

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjList(numCourses);
        for (auto& item : prerequisites) {
            adjList[item[0]].push_back(item[1]);
        }

        vector<bool> visited(numCourses);
        vector<bool> path(numCourses);
        for (int i = 0; i < numCourses; i++) {
            if (!visited[i]) {
                bool res = dfs(i, adjList, visited, path);
                if (!res) return false;
            }
        }

        return true;
    }
};
