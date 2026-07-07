class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> st;
        for (auto op : operations) {
            if (op == "+") {
                int first = st.top();
                st.pop();
                int sec = st.top();
                st.push(first);
                st.push(first + sec);
            } else if (op == "D") {
                int t = st.top();
                st.push(t *= 2);
            } else if (op == "C") {
                st.pop();
            } else {
                st.push(stoi(op));
            }
        }

        int sum = 0;
        while (!st.empty()) {
            int val = st.top();
            sum += val;
            st.pop();
        }

        return sum;
    }
};