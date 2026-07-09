/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int count = 0, res = 0, l = 0, r = 0;
        vector<int> startArr, endArr;

        for (const auto& i : intervals) {
            startArr.push_back(i.start);
            endArr.push_back(i.end);
        }

        sort(startArr.begin(), startArr.end());
        sort(endArr.begin(), endArr.end());

        while (l < intervals.size()) {
            if (startArr[l] < endArr[r]) {
                l++;
                count++;
            } else {
                r++;
                count--;
            }

            res = max(res, count);
        }

        return res;
    }
};
