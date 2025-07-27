# Problem 19: Remove Nth Node From End of List
# Difficulty: Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        if not head:
            return None
        curr = head
        prev = None
        while curr:
            lst.append((prev, curr))
            prev = curr
            curr = curr.next
        prev, curr = lst[len(lst) - n]
        if prev == None:
            head = head.next
            curr.next = None
        else:
            prev.next = curr.next
            curr.next = None
        return head