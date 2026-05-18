class Solution {
public:

    string encode(vector<string>& strs) {
        string s;
        for(const auto &str : strs){
            s += to_string(str.length()) + '#' + str;
        }

        return s;
    }

    vector<string> decode(string s) {
        vector<string> result;

        int i = 0;
        while(i < s.length()){
            int len = 0;
            while(s[i] != '#'){
                len = len*10 + (s[i] - '0');
                i++;
            }
            i++;
            result.push_back(s.substr(i, len));
            i = i+len;
        }
        
        return result;
    }

};