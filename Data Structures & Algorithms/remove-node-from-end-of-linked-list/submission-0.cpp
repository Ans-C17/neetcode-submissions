/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* run = head;
        int size = 1;
        while(run->next){
            run = run->next;
            size++;
        }

        if(size-n == 0) return head->next;

        run = head;
        for(int i = 1; i < (size-n); i++) run = run->next;
        run->next = run->next->next;
        return head;
    }
};
