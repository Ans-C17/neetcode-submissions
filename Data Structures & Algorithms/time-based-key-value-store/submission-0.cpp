class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> keyVals;

public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        keyVals[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        if(keyVals[key].empty()) return "";

        int low = 0;
        int high = keyVals[key].size() - 1;
        int minIndex = -1;
        while(low <= high){
            int mid = low + (high - low)/2;
            if(keyVals[key][mid].first <= timestamp){
                minIndex = max(minIndex, mid);
                low = mid + 1;
            }else high = mid - 1;
        }

        if(minIndex == -1) return "";
        return keyVals[key][minIndex].second;
    }
};
