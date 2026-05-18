class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if(s1.length() > s2.length()) return false;

        vector<int> s1count(26, 0);
        vector<int> s2count(26, 0);

        for(int i = 0; i < s1.length(); i++){
            s1count[s1[i] - 'a']++;
            s2count[s2[i] - 'a']++;
        }

        int matches = 0;
        for(int i = 0; i < 26; i++){
            if(s1count[i] == s2count[i]) matches++;
        }

        int left = 0;
        for(int right = s1.length(); right < s2.length(); right++){
            if(matches == 26) return true;

            int index = s2[right] - 'a';
            s2count[index]++;
            if(s1count[index] == s2count[index]) matches++;
            else if(s1count[index]+1 == s2count[index]) matches--;

            index = s2[left] - 'a';
            s2count[index]--;
            if(s1count[index] == s2count[index]) matches++;
            else if(s1count[index]-1 == s2count[index]) matches--;

            left++;
        }

        return matches == 26;
    }
};
