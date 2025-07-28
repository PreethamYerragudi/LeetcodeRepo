# Problem 876: Middle of the Linked List
# Difficulty: Easy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #use two algorithms, one for odd number length 
        slow = head 
        fast = head
        
        while fast and fast.next: 
            slow = slow.next #increment by 1 
            fast = fast.next.next #increment by 2
            print("here is slow", slow)
            print("here is fast", slow)
        

        return slow #return the pointer 