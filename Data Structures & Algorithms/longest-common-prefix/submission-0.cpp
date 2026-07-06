class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = strs[0];
        for (int i = 1; i < strs.size(); i++) {
            string curr = "";
            int len = max(res.length(), strs[i].length());
            for (int j = 0; j < len; j++) {
                if (res[j] != strs[i][j]) {
                    break;
                }

                curr += res[j];
            }

            res = curr;
        }

        return res;
    }
};