# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1, p2 = l1, l2
        dummy = ListNode()
        cur = dummy

        while p1 and p2:
            total = p1.val + p2.val + carry
            down = total % 10
            carry = total // 10
            newNode = ListNode(down)
            cur.next = newNode
            cur = newNode
            p1, p2 = p1.next, p2.next
        
        while p1 or p2:
            if p1:
                total = p1.val + carry
                down = total % 10
                newNode = ListNode(down)
                p1 = p1.next
            else:
                total = p2.val + carry
                down = total % 10
                newNode = ListNode(down)
                p2 = p2.next
            
            carry = total // 10
            cur.next = newNode
            cur = newNode
        
        if carry:
            newNode = ListNode(carry)
            cur.next = newNode

        return dummy.next