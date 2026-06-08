# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prv, cur, nxt = None, slow.next, slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt

        p1 = head
        p2 = prv

        while p2:
            tmp, pmt = p1.next, p2.next
            p1.next = p2
            p2.next = tmp
            p1, p2 = tmp, pmt

