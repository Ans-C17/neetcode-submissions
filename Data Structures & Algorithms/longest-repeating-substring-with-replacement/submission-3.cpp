class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> hash;

        int left = 0;
        int maxElem = 0;
        int maxLen = 0;
        for(int right = 0; right < s.length(); right++){
            hash[s[right]]++;
            for(const auto& letter : hash) maxElem = max(maxElem, letter.second);
            while((right-left+1) - maxElem > k){
                hash[s[left]]--;
                left++;
            }

            maxLen = max(right-left+1, maxLen);
        }

        return maxLen;
    }
};
