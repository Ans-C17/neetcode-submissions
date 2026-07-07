class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if (hand.size() % groupSize) {
            return false;
        }

        unordered_map<int, int> hashmap;
        for (auto h : hand) {
            hashmap[h]++;
        }

        vector<int> keys;
        for (auto [key, val] : hashmap) {
            keys.push_back(key);
        }

        priority_queue<int, vector<int>, greater<int>> minHeap(keys.begin(), keys.end());
        while (!minHeap.empty()) {
            int first = minHeap.top();
            for (int i = first; i < first + groupSize; i++) {
                if (hashmap.find(i) == hashmap.end()) {
                    return false;
                }

                hashmap[i]--;
                if (hashmap[i] == 0) {
                    if (i != minHeap.top()) {
                        return false;
                    }

                    minHeap.pop();
                }
            }
        }

        return true;
    }
};
