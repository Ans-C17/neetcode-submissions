class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> posspeed;

        for(int i = 0; i < position.size(); i++){
            posspeed.push_back({position[i], speed[i]});
        }

        sort(posspeed.rbegin(), posspeed.rend());

        vector<double> stack;
        for(const auto& elem : posspeed){
            stack.push_back((double)(target - elem.first)/elem.second);
            if(stack.size() >= 2 && stack.back() <= stack[stack.size()-2]){
                stack.pop_back();
            }
        }

        return stack.size();
    }
};
