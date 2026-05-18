# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        length = 0
        while fast:
            fast = fast.next
            length += 1
        
        if n == length:
            return head.next
        
        target = length - n  - 1
        for i in range(target):
            slow = slow.next
        
        slow.next = slow.next.next
        
        return head