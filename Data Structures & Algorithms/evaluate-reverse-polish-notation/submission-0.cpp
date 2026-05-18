class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        int ans = 0;
        for(string k : tokens){
            if(k == "+" || k == "-" || k == "/" || k == "*"){
                int a = s.top();
                s.pop();
                if(k == "+") s.top() += a;
                if(k == "-") s.top() -= a;
                if(k == "*") s.top() *= a;
                if(k == "/") s.top() /= a;
            }else{
                s.push(stoi(k));
            }
        }

        return s.top();
    }
};
