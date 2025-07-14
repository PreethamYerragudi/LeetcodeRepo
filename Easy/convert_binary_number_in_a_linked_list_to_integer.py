# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        curr = head
        bin_str = ""
        while curr:
            bin_str += str(curr.val)
            curr = curr.next
        return int(bin_str, 2)
