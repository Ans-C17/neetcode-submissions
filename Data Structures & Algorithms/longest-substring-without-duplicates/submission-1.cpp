class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> hash;

        int left = 0;
        int right = 0;

        if(s.length() == 0) return 0;

        int maxLength = 0;
        while(right < s.length()){
            if(hash.count(s[right])){
                while(s[left] != s[right]){
                    hash.erase(s[left]);
                    left++;
                }
                left++;
            }

            hash.insert(s[right]);
            maxLength = max(maxLength, (int)hash.size());
            right++;
        }

        return maxLength;
    }
};
