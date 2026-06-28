# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        curr = head
        last = ListNode(val=head.val)
        while curr and curr.next:
            last = ListNode(val=curr.next.val, next=last)
            curr = curr.next
        return last