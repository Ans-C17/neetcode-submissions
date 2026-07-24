class Solution {
public:
    vector<string> children(string node) {
        vector<string> res;
        for (int i = 0; i < 4; i++) {
            string copy = node;
            copy[i] = ((copy[i] - '0') + 1) % 10 + '0';
            res.push_back(copy);

            copy = node;
            copy[i] = ((copy[i] - '0') - 1 + 10) % 10 + '0';
            res.push_back(copy);
        }

        return res;
    }

    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> dead;
        for (auto& d : deadends) dead.insert(d);

        if (dead.count("0000")) return -1;

        queue<pair<string, int>> q;
        q.push({"0000", 0});
        dead.insert("0000");
        while (!q.empty()) {
            string node = q.front().first;
            int moves = q.front().second;
            q.pop();
            if (node == target) return moves;
            for (auto child : children(node)) {
                if (!dead.count(child)) {
                    dead.insert(child);
                    q.push({child, moves + 1});
                }
            }
        }

        return -1;
    }
};