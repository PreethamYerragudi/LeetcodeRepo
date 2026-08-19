# Problem 2: Add Two Numbers
# Difficulty: Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        curr = head
        while l1 or l2:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            carry = s >= 10
            s = s % 10
            curr.val = s
            if l1 or l2:
                curr.next = ListNode()
                curr = curr.next
        if carry:
            curr.next = ListNode(1)
            
        return head
        
            
