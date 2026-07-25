class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adjList(numCourses);
        vector<int> indegree(numCourses, 0);
        for (auto& item : prerequisites) {
            adjList[item[1]].push_back(item[0]);
            indegree[item[0]]++;
        }

        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0)
                q.push(i);
        }

        while (!q.empty()) {
            int prereq = q.front();
            q.pop();
            for (int nei : adjList[prereq]) {
                indegree[nei]--;
                if (indegree[nei] == 0) q.push(nei);
            }
        }

        for (int i : indegree) {
            if (i != 0) return false;
        }

        return true;
    }
};
