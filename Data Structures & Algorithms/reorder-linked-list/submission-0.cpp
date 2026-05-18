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
    void reorderList(ListNode* head) {
        if(!head->next || !head->next->next) return;

        ListNode* slow = head;
        ListNode* fast = head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode *prev = nullptr;
        ListNode *curr = slow;
        ListNode *next = slow;
        while(curr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        ListNode *headNext;
        ListNode *prevPrev;
        while(prev && prev->next){
            headNext = head->next;
            prevPrev = prev->next;
            head->next = prev;
            prev->next = headNext;
            head = headNext;
            prev = prevPrev;
        }

        return;
    }
};
