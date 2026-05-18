class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        if(s[0] == ')' || s[0] == '}' || s[0] == ']') return false;
        for(char k : s){
            if(k == '(' || k == '{' || k == '['){
                st.push(k);
            }else if(k == ')'){
                if(!st.empty() && st.top() == '(') st.pop();
                else return false;
            }else if(k == '}'){
                if(!st.empty() && st.top() == '{') st.pop();
                else return false;
            }else if(k == ']'){
                if(!st.empty() && st.top() == '[') st.pop();
                else return false;
            }
        }

        if(st.empty()) return true;
        return false;
    }
};
