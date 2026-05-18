class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26, 0);
        for(const auto& task : tasks) count[task - 'A']++;

        priority_queue<int> maxHeap;
        for(const auto& elem : count) if(elem > 0) maxHeap.push(elem);

        int time = 0;
        queue<pair<int, int>> q;
        while(!maxHeap.empty() || !q.empty()){ //randum empty ayale answer vendu
            time++;
            if(maxHeap.empty()) time = q.front().second;
            //above step is to skip idle time and get the next time directly.. optimisation aan
            else{
                //remove elements from the heap
                if(maxHeap.top()-1 > 0) q.push({maxHeap.top()-1, time+n});
                maxHeap.pop();
            }

            //then add elements to the heap
            if(!q.empty() && q.front().second == time){
                maxHeap.push(q.front().first);
                q.pop();
            }
        }

        return time;
    }
};
