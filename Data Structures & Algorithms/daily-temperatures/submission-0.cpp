class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ans(temperatures.size(), 0);
        stack<pair<int, int>> s;

        for(int i = 0; i < temperatures.size(); i++){
            while(!s.empty() && temperatures[i] > s.top().first){
                auto pair = s.top();
                s.pop();
                ans[pair.second] = i - pair.second;
            }

            s.push({temperatures[i], i});
        }

        return ans;
    }
};
