class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;
        for(const auto& stone : stones) maxHeap.push(stone);
        for(int i = 1; i < stones.size(); i++){
            int top = maxHeap.top();
            maxHeap.pop();
            int second = maxHeap.top();
            maxHeap.pop();
            
            maxHeap.push(top-second);
        }

        return !maxHeap.empty() ? maxHeap.top() : 0;
    }
};
