class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.empty() && t.empty()) return true;
        if((s.empty() && !t.empty()) || (!s.empty() && t.empty())) return false;

        unordered_map<char, int> freq;
        for(char letter : s) freq[letter]++;
        for(char letter : t){
            if(freq[letter] > 0) freq[letter]--;
            else return false;
        }

        for(char letter : t){
            if(freq[letter] != 0) return false;
        }
        for(char letter :s){
            if(freq[letter] != 0) return false;
        }
        return true;
    }
};
