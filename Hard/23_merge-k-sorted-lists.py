# Problem 23: Merge k Sorted Lists
# Difficulty: Hard
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) < 1:
            return None
        m = len(lists) // 2
        left = self.mergeKLists(lists[0:m])
        right = self.mergeKLists(lists[m: len(lists)])
        head = None
        curr = None
        while left and right:
            if left.val < right.val:
                if not head:
                    head = left
                    curr = head
                    left = left.next
                else:
                    curr.next = left
                    curr = curr.next
                    left = left.next
            else:
                if not head:
                    head = right
                    curr = head
                    right = right.next
                else:
                    curr.next = right
                    curr = curr.next
                    right = right.next
        while left:
            if not head:
                return left
            curr.next = left
            curr = curr.next
            left = left.next
        while right:
            if not head:
                return right
            curr.next = right
            curr = curr.next
            right = right.next

        return head
