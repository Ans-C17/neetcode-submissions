class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for(int num : nums){
            minHeap.push(num); //push the element and let it heapify
            //now the smallest element will be at the top
            if(minHeap.size() > k) minHeap.pop();
            //heapify will automatically be called after pop()
        }
    }
    
    int add(int val) {
        minHeap.push(val);
        if(minHeap.size() > k) minHeap.pop();
        return minHeap.top();
    }
};
