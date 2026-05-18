class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hash;
        for(const auto& s : strs){
            vector<int> count(26, 0);
            for(const auto& letter : s) count[letter - 'a']++;

            string code = to_string(count[0]);
            for(int i = 1; i < 26; ++i){
                code += ',' + to_string(count[i]);
            }

            hash[code].push_back(s);
        }

        vector<vector<string>> answer;
        for(const auto& element : hash){
            answer.push_back(element.second);
        }

        return answer;
    }
};
